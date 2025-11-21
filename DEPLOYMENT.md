# Deployment Guide

## Deploying to Railway (Recommended)

Railway is the easiest way to deploy this app to production.

### Prerequisites
1. Create a [Railway account](https://railway.app/) (free, sign in with GitHub)
2. Push your code to a GitHub repository

### Deployment Steps

#### 1. Connect to Railway
```bash
# Install Railway CLI (optional, but helpful)
npm i -g @railway/cli
# Or use homebrew
brew install railway
```

#### 2. Deploy via Railway Dashboard (Easiest)
1. Go to [railway.app](https://railway.app/)
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose your `warcraftlogs` repository
5. Railway will automatically detect it's a Python app and deploy!

#### 3. Deploy via CLI (Alternative)
```bash
# Login to Railway
railway login

# Initialize project (in your repo directory)
railway init

# Deploy
railway up
```

#### 4. Monitor Deployment
- Railway will automatically:
  - Install dependencies from `requirements.txt`
  - Use Python version from `runtime.txt` (3.12.3)
  - Start uWSGI using the `Procfile`
  - Assign a public URL (e.g., `yourapp.railway.app`)

#### 5. View Your Live App
- Click on the deployment in Railway dashboard
- Copy the public URL
- Your app is live! 🎉

### Configuration Files for Railway
- **Procfile**: Tells Railway how to start the app
- **runtime.txt**: Specifies Python 3.12.3
- **railway.toml**: Optional Railway-specific config
- **requirements.txt**: Python dependencies

### Adding a Custom Domain (Optional)
1. In Railway dashboard, go to your service
2. Click "Settings" → "Domains"
3. Click "Custom Domain"
4. Add your domain and update DNS records

### Environment Variables
If you need to add environment variables (API keys, etc.):
1. Railway dashboard → Your service → "Variables"
2. Add key-value pairs
3. Railway auto-redeploys on changes

### Viewing Logs
```bash
# Via CLI
railway logs

# Or in Railway dashboard → Deployments → Click deployment → View logs
```

### Costs
- **Free tier**: $5 credit per month
- Typical usage for this app: ~$3-5/month
- If you exceed free tier, it's pay-as-you-go

---

## Running with uWSGI

### Local Development
```bash
# Still use Flask's built-in server for development
python app.py
# Or enable debug mode
FLASK_DEBUG=true python app.py
```

### Production with uWSGI

#### 1. Install dependencies
```bash
pip install -r requirements.txt
```

#### 2. Run uWSGI directly (for testing)
```bash
# Using the config file
uwsgi --ini uwsgi.ini

# Or with command line options
uwsgi --http 0.0.0.0:8000 --module wsgi:app --processes 4 --threads 2
```

#### 3. Run as a system service (recommended)

Create `/etc/systemd/system/warcraftlogs.service`:
```ini
[Unit]
Description=WarcraftLogs Analysis uWSGI
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/warcraftlogs
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/uwsgi --ini uwsgi.ini

[Install]
WantedBy=multi-user.target
```

Then:
```bash
sudo systemctl daemon-reload
sudo systemctl start warcraftlogs
sudo systemctl enable warcraftlogs
sudo systemctl status warcraftlogs
```

#### 4. Set up Nginx reverse proxy (optional but recommended)
```bash
# Copy example config
sudo cp nginx.conf.example /etc/nginx/sites-available/warcraftlogs
# Edit the file to update paths and domain
sudo nano /etc/nginx/sites-available/warcraftlogs
# Enable site
sudo ln -s /etc/nginx/sites-available/warcraftlogs /etc/nginx/sites-enabled/
# Test and reload
sudo nginx -t
sudo systemctl reload nginx
```

## Configuration Explanation

### uwsgi.ini settings:
- **processes = 4**: Runs 4 worker processes (adjust based on CPU cores)
- **threads = 2**: Each process has 2 threads (8 concurrent requests total)
- **harakiri = 60**: Kills requests taking longer than 60 seconds
- **max-requests = 1000**: Respawns workers after 1000 requests (prevents memory leaks)
- **buffer-size = 32768**: Handles larger requests/responses

### Socket vs HTTP:
- Use **socket** mode with Nginx reverse proxy (more efficient)
- Use **http** mode for direct access without Nginx

## Monitoring

```bash
# View logs
tail -f /tmp/uwsgi.log

# Check service status
sudo systemctl status warcraftlogs

# View Nginx logs
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log
```

## Troubleshooting

### uWSGI won't start
- Check file permissions
- Verify Python path in systemd service
- Check logs: `journalctl -u warcraftlogs -f`

### 502 Bad Gateway (Nginx)
- Ensure uWSGI is running
- Verify socket/port matches between uwsgi.ini and nginx.conf
- Check Nginx error logs

### High memory usage
- Reduce number of processes/threads
- Lower max-requests value to recycle workers more frequently
