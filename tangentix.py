import dash
from dash import dcc, html, Input, Output, State, ctx
import numpy as np
import plotly.graph_objects as go
import sympy as sp
from sympy.calculus.util import continuous_domain

# Configuration de l'application
app = dash.Dash(__name__)

x_sym = sp.symbols('x')

# --- Styles CSS ---
dark_style = {
    'backgroundColor': '#0b0e14',
    'color': '#E0E0E0',
    'padding': '20px',
    'minHeight': '100vh',
    'fontFamily': 'Segoe UI, Roboto, sans-serif'
}

# Style des boutons du clavier
btn_style = {
    'backgroundColor': '#21262d',
    'color': '#58a6ff',
    'border': '1px solid #30363d',
    'borderRadius': '6px',
    'padding': '10px',
    'fontSize': '18px',
    'cursor': 'pointer',
    'fontWeight': 'bold',
    'transition': '0.2s'
}

# --- Mise en page (Layout) ---
app.layout = html.Div(style=dark_style, children=[
    html.H1("🚀 Tangentix ", style={'textAlign': 'center', 'color': '#58a6ff', 'marginBottom': '30px'}),

    # Conteneur de Saisie (Largeur 95%)
    html.Div([
        
        # 1. CLAVIER MATHÉMATIQUE
        html.Div([
            html.Button("x²", id={'type': 'm-btn', 'val': '**2'}, style=btn_style),
            html.Button("√x", id={'type': 'm-btn', 'val': 'sqrt('}, style=btn_style),
            html.Button("eˣ", id={'type': 'm-btn', 'val': 'exp('}, style=btn_style),
            html.Button("ln", id={'type': 'm-btn', 'val': 'ln('}, style=btn_style),
            html.Button("sin", id={'type': 'm-btn', 'val': 'sin('}, style=btn_style),
            html.Button("cos", id={'type': 'm-btn', 'val': 'cos('}, style=btn_style),
            html.Button("π", id={'type': 'm-btn', 'val': 'pi'}, style=btn_style),
            html.Button("/", id={'type': 'm-btn', 'val': '/'}, style=btn_style),
            html.Button("(", id={'type': 'm-btn', 'val': '('}, style=btn_style),
            html.Button(")", id={'type': 'm-btn', 'val': ')'}, style=btn_style),
        ], style={
            'display': 'grid', 
            'gridTemplateColumns': 'repeat(10, 1fr)', 
            'gap': '10px', 
            'marginBottom': '15px'
        }),

        # 2. ZONE DE SAISIE
        dcc.Textarea(
            id='func-input',
            value='exp(x) - 2*x**2 - 6*x + 3',
            style={
                'width': '100%', 'height': '100px', 'padding': '15px',
                'backgroundColor': '#161b22', 'color': '#58a6ff',
                'border': '2px solid #30363d', 'borderRadius': '10px',
                'fontSize': '22px', 'fontFamily': 'monospace', 'outline': 'none'
            }
        ),

        # 3. APERÇU MATHÉMATIQUE (LaTeX Live)
        html.Div(id='latex-preview', style={
            'marginTop': '15px', 'padding': '15px', 'backgroundColor': '#1A1A1A',
            'borderRadius': '8px', 'borderLeft': '5px solid #58a6ff', 'fontSize': '20px'
        }),

    ], style={'width': '95%', 'margin': '0 auto 30px auto'}),

    # 4. SLIDER
    html.Div([
        html.Label("📍 Position de la tangente (x₀) :", style={'color': '#ffa657', 'fontWeight': 'bold'}),
        dcc.Slider(
            id='x0-slider', min=-10, max=10, step=0.1, value=0,
            marks={i: {'label': str(i), 'style': {'color': '#8b949e'}} for i in range(-10, 11, 2)}
        ),
    ], style={'width': '95%', 'margin': '0 auto 40px auto'}),

    # 5. GRILLE : GRAPHIQUE + ANALYSE
    html.Div([
        # Colonne Graphique
        html.Div([
            dcc.Graph(id='main-graph', style={'height': '65vh'})
        ], style={'flex': '2'}),

        # Colonne Analyse
        html.Div([
            html.H3("📊 Analyse Détaillée", style={'color': '#58a6ff', 'borderBottom': '1px solid #30363d'}),
            dcc.Markdown(id='math-results', mathjax=True)
        ], style={
            'flex': '1', 'backgroundColor': '#161b22', 'padding': '20px', 
            'borderRadius': '10px', 'marginLeft': '20px', 'overflowY': 'auto', 'maxHeight': '65vh'
        }),
    ], style={'display': 'flex', 'flexWrap': 'wrap', 'width': '95%', 'margin': '0 auto'})
])

# --- CALLBACK 1 : Gestion du Clavier ---
@app.callback(
    Output('func-input', 'value'),
    Input({'type': 'm-btn', 'val': dash.ALL}, 'n_clicks'),
    State('func-input', 'value'),
    prevent_initial_call=True
)
def update_input(n_clicks, current_value):
    if not any(n_clicks): return current_value
    
    # Identifie quel bouton a été cliqué
    triggered_id = ctx.triggered_id
    symbol = triggered_id['val']
    
    return f"{current_value}{symbol}"

# --- CALLBACK 2 : Calculs et Graphique ---
@app.callback(
    [Output('main-graph', 'figure'),
     Output('math-results', 'children'),
     Output('latex-preview', 'children')],
    [Input('func-input', 'value'),
     Input('x0-slider', 'value')]
)
def update_app(func_str, x0):
    try:
        # Nettoyage et SymPy
        f_expr = sp.sympify(func_str.replace('^', '**'))
        f_prime = sp.diff(f_expr, x_sym)
        f_double = sp.diff(f_prime, x_sym)
        domaine = continuous_domain(f_expr, x_sym, sp.S.Reals)
        
        # Aperçu LaTeX
        preview = dcc.Markdown(f"**Expression reconnue :** $f(x) = {sp.latex(f_expr)}$", mathjax=True)

        # Graphique
        f_num = sp.lambdify(x_sym, f_expr, "numpy")
        x_vals = np.linspace(-15, 15, 1000)
        with np.errstate(all='ignore'):
            y_vals = f_num(x_vals)
            y_vals = np.where(np.abs(y_vals) < 1e6, y_vals, np.nan)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_vals, y=y_vals, name="f(x)", line=dict(color='#58a6ff', width=3)))
        
        # Tangente
        y0 = float(f_expr.subs(x_sym, x0).evalf())
        slope = float(f_prime.subs(x_sym, x0).evalf())
        y_tangent = slope * (x_vals - x0) + y0
        fig.add_trace(go.Scatter(x=x_vals, y=y_tangent, name="Tangente", line=dict(color='#ffa657', dash='dot')))
        fig.add_trace(go.Scatter(x=[x0], y=[y0], mode='markers', marker=dict(color='#ff7b72', size=12)))

        fig.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

        # Analyse
        res = [
            f"**Domaine :** ${sp.latex(domaine)}$",
            f"**Dérivée :** $f'(x) = {sp.latex(f_prime)}$",
            f"**Dérivée seconde :** $f''(x) = {sp.latex(f_double)}$",
            f"---",
            f"**Limites :**",
            f"- $x \\to -\\infty : {sp.latex(sp.limit(f_expr, x_sym, -sp.oo))}$",
            f"- $x \\to +\\infty : {sp.latex(sp.limit(f_expr, x_sym, sp.oo))}$",
            f"---",
            f"**Tangente en $x_0 = {x0}$ :**",
            f"$y = {round(slope, 2)}x + {round(y0 - slope*x0, 2)}$"
        ]
        
        return fig, "\n\n".join(res), preview
    
    except Exception as e:
        return go.Figure().update_layout(template="plotly_dark"), f"⚠️ Erreur : {e}", "Saisie incomplète..."

if __name__ == "__main__":
    app.run(debug=True)
