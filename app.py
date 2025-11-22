from flask import Flask, render_template, jsonify, request
import pandas as pd
import os
import re
from analyze_druid import analyze_druid_performance

app = Flask(__name__)

# Available datasets
DATASETS = {
    'brutallus': 'data/t6/brutallus.csv',
    'felmyst': 'data/t6/felmyst.csv'
}

def load_data(dataset='brutallus'):
    """Load and return the specified dataset"""
    data_path = DATASETS.get(dataset)
    if data_path and os.path.exists(data_path):
        df = pd.read_csv(data_path)
        # Convert numeric columns to appropriate types
        numeric_cols = ['HPS', 'Haste', 'Spirit', 'Intellect']
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        return df
    return None

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    """API endpoint to get the full dataset"""
    dataset = request.args.get('dataset', 'brutallus')
    df = load_data(dataset)
    if df is not None:
        # Replace NaN with None for proper JSON serialization
        return jsonify(df.where(pd.notna(df), None).to_dict(orient='records'))
    return jsonify({'error': 'Data not found'}), 404

@app.route('/api/stats')
def get_stats():
    """API endpoint to get summary statistics"""
    dataset = request.args.get('dataset', 'brutallus')
    df = load_data(dataset)
    if df is None:
        return jsonify({'error': 'Data not found'}), 404

    stats = {
        'total_records': len(df),
        'avg_hps': df['HPS'].mean() if 'HPS' in df.columns else 0,
        'max_hps': df['HPS'].max() if 'HPS' in df.columns else 0,
        'min_hps': df['HPS'].min() if 'HPS' in df.columns else 0,
        'avg_haste': df['Haste'].mean() if 'Haste' in df.columns else 0,
        'avg_spirit': df['Spirit'].mean() if 'Spirit' in df.columns else 0,
        'avg_intellect': df['Intellect'].mean() if 'Intellect' in df.columns else 0,
    }

    return jsonify(stats)

@app.route('/api/top/<int:n>')
def get_top_n(n):
    """API endpoint to get top N healers by HPS"""
    dataset = request.args.get('dataset', 'brutallus')
    natures_grace_filter = request.args.get('naturesGrace', None)
    total_healers_filter = request.args.get('totalHealers', None)
    vampiric_touch_filter = request.args.get('vampiricTouch', None)
    innervates_filter = request.args.get('innervates', None)
    rotating_on_tank_filter = request.args.get('rotatingOnTank', None)
    n_druid_filter = request.args.get('nDruid', None)
    n_paladin_filter = request.args.get('nPaladin', None)
    n_hpriest_filter = request.args.get('nHPriest', None)
    n_dpriest_filter = request.args.get('nDPriest', None)
    n_shaman_filter = request.args.get('nShaman', None)
    regions_filter = request.args.get('regions', None)

    df = load_data(dataset)
    if df is None:
        return jsonify({'error': 'Data not found'}), 404

    # Filter out HPS = 0.0
    df = df[df['HPS'] > 0]

    # Apply regions filter if specified
    if regions_filter:
        allowed_regions = regions_filter.split(',')
        df = df[df['Region'].isin(allowed_regions)]

    # Apply NaturesGrace filter if specified
    if natures_grace_filter in ['Yes', 'No']:
        df = df[df['NaturesGrace'] == natures_grace_filter]

    # Apply TotalHealers filter if specified
    if total_healers_filter and total_healers_filter.isdigit():
        df = df[df['TotalHealers'] == int(total_healers_filter)]

    # Apply VampiricTouch filter if specified
    if vampiric_touch_filter in ['Yes', 'No']:
        df = df[df['VampiricTouch'] == vampiric_touch_filter]

    # Apply Innervates filter if specified
    if innervates_filter and innervates_filter.isdigit():
        df = df[df['InnervateCount'] == int(innervates_filter)]

    # Apply RotatingOnTank filter if specified
    if rotating_on_tank_filter in ['Yes', 'No']:
        df = df[df['RotatingOnTank'] == rotating_on_tank_filter]

    # Apply healer composition filters if specified
    if n_druid_filter and n_druid_filter.isdigit():
        df = df[df['nDruid'] == int(n_druid_filter)]

    if n_paladin_filter and n_paladin_filter.isdigit():
        df = df[df['nPaladin'] == int(n_paladin_filter)]

    if n_hpriest_filter and n_hpriest_filter.isdigit():
        df = df[df['nHPriest'] == int(n_hpriest_filter)]

    if n_dpriest_filter and n_dpriest_filter.isdigit():
        df = df[df['nDPriest'] == int(n_dpriest_filter)]

    if n_shaman_filter and n_shaman_filter.isdigit():
        df = df[df['nShaman'] == int(n_shaman_filter)]

    # Store total count before limiting
    total_count = len(df)

    top_n = df.head(n)

    # Add adjusted rank (1-indexed position in filtered results)
    top_n = top_n.copy()
    top_n['AdjustedRank'] = range(1, len(top_n) + 1)

    # Replace NaN with None for proper JSON serialization
    data_records = top_n.where(pd.notna(top_n), None).to_dict(orient='records')

    # Return both data and total count
    return jsonify({
        'data': data_records,
        'total_count': total_count
    })

@app.route('/api/analyze-report', methods=['POST'])
def analyze_report():
    """API endpoint to analyze a specific report for a player"""
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    report_input = data.get('report_code', '').strip()
    boss_name = data.get('boss_name', '').strip()
    player_name = data.get('player_name', '').strip()

    # Validate required fields
    if not report_input:
        return jsonify({'error': 'Report code is required'}), 400
    if not boss_name:
        return jsonify({'error': 'Boss name is required'}), 400
    if not player_name:
        return jsonify({'error': 'Player name is required'}), 400

    # Extract report code from URL if a full URL was provided
    report_code = report_input
    url_match = re.search(r'warcraftlogs\.com/reports/([a-zA-Z0-9]+)', report_input)
    if url_match:
        report_code = url_match.group(1)

    try:
        # Call the analysis function
        result = analyze_druid_performance(report_code, boss_name, player_name)

        # Convert datetime-like fields for JSON serialization
        from datetime import datetime

        # Build response with formatted data
        response_data = {
            'success': True,
            'report_code': report_code,
            'fight_id': result['fight_id'],
            'player_id': result['player_id'],
            'is_kill': result['is_kill'],
            'date': datetime.fromtimestamp(result['timestamp'] / 1000).strftime("%Y-%m-%d"),
            'duration': f"{result['duration_minutes']}m {result['duration_seconds']}s",
            'duration_minutes': result['duration_minutes'],
            'duration_seconds': result['duration_seconds'],
            'total_healers': result['total_healers'],
            'healer_composition': result['healer_composition'],
            'raid_damage_taken_per_second': result['raid_damage_taken_per_second'],
            'player_name': result['player_name'],
            'player_stats': result['player_stats'],
            'player_trinkets': result['player_trinkets'],
            'player_ranking': result['player_ranking'],
            'has_vampiric_touch': result['has_vampiric_touch'],
            'innervate_count': result['innervate_count'],
            'has_bloodlust': result['has_bloodlust'],
            'has_natures_grace': result['has_natures_grace'],
            'lifebloom_uptime_percent': result['lifebloom_uptime_percent'],
            'lifebloom_hps': result['lifebloom_hps'],
            'rejuvenation_hps': result['rejuvenation_hps'],
            'regrowth_total_hps': result['regrowth_total_hps'],
            'regrowth_by_rank': result['regrowth_by_rank'],
            'tanks': result['tanks'],
            'rotation_count': result['rotation_count'],
            'actual_rotations': result['actual_rotations'],
            'sorted_patterns': result['sorted_patterns'],
            'tank_rotation_percent': result['tank_rotation_percent'],
            'rotating_on_tank': result['rotating_on_tank'],
            'cast_data': result['cast_data'],
            'report_link': f"https://classic.warcraftlogs.com/reports/{report_code}?fight={result['fight_id']}&source={result['player_id']}&type=healing"
        }

        return jsonify(response_data)

    except Exception as e:
        error_message = str(e)

        # Provide more user-friendly error messages
        if 'not found' in error_message.lower():
            return jsonify({'error': f'Could not find the specified data: {error_message}'}), 404
        elif 'token' in error_message.lower() or 'auth' in error_message.lower():
            return jsonify({'error': 'Authentication error. Please ensure your WarcraftLogs credentials are configured.'}), 401
        elif 'rate limit' in error_message.lower():
            return jsonify({'error': 'Rate limit exceeded. Please wait a few minutes and try again.'}), 429
        else:
            return jsonify({'error': f'Analysis failed: {error_message}'}), 500


if __name__ == '__main__':
    # Only for local development - use uWSGI for production
    import os
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
