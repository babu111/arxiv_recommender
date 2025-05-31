import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Configure for deployment - always use mock data
IS_DEPLOYMENT = True  # Always true for demo version

# Mock data for deployment
MOCK_PAPERS = [
    {
        "id": 1,
        "title": "Attention Is All You Need",
        "authors": "Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin",
        "abstract": "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train.",
        "categories": "cs.CL, cs.AI, cs.LG",
        "published_date": "2017-06-12T17:35:22Z",
        "arxiv_id": "1706.03762",
        "pdf_url": "https://arxiv.org/pdf/1706.03762.pdf"
    },
    {
        "id": 2,
        "title": "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
        "authors": "Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova",
        "abstract": "We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers. Unlike recent language representation models, BERT is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be fine-tuned with just one additional output layer to create state-of-the-art models for a wide range of tasks.",
        "categories": "cs.CL",
        "published_date": "2018-10-11T18:37:45Z",
        "arxiv_id": "1810.04805",
        "pdf_url": "https://arxiv.org/pdf/1810.04805.pdf"
    },
    {
        "id": 3,
        "title": "Deep Learning for Natural Language Processing",
        "authors": "John Smith, Jane Doe, Bob Johnson",
        "abstract": "This paper presents a comprehensive survey of deep learning techniques applied to natural language processing tasks. We review the latest advances in neural architectures, training methods, and evaluation metrics. Our analysis covers applications in machine translation, text classification, sentiment analysis, and question answering systems.",
        "categories": "cs.CL, cs.LG, cs.AI",
        "published_date": "2024-12-15T10:30:00Z",
        "arxiv_id": "2412.12345",
        "pdf_url": "https://arxiv.org/pdf/2412.12345.pdf"
    },
    {
        "id": 4,
        "title": "Generative Pre-trained Transformers: A Paradigm Shift in AI",
        "authors": "Alice Wang, Charlie Brown, Diana Chen",
        "abstract": "Large language models have revolutionized artificial intelligence applications across multiple domains. This work examines the architectural innovations, training methodologies, and emergent capabilities of generative pre-trained transformers. We discuss their impact on natural language understanding, code generation, and creative applications.",
        "categories": "cs.AI, cs.CL, cs.LG",
        "published_date": "2024-12-10T14:22:30Z",
        "arxiv_id": "2412.10987",
        "pdf_url": "https://arxiv.org/pdf/2412.10987.pdf"
    },
    {
        "id": 5,
        "title": "Quantum Machine Learning: Bridging Two Revolutionary Fields",
        "authors": "Emma Physics, Frank Quantum, Grace Computing",
        "abstract": "Quantum computing promises exponential speedups for certain computational problems. This survey explores the intersection of quantum computing and machine learning, reviewing quantum algorithms for optimization, quantum neural networks, and hybrid classical-quantum approaches to learning.",
        "categories": "quant-ph, cs.LG, cs.AI",
        "published_date": "2024-12-08T09:15:45Z",
        "arxiv_id": "2412.08765",
        "pdf_url": "https://arxiv.org/pdf/2412.08765.pdf"
    },
    {
        "id": 6,
        "title": "Neural Architecture Search: Automating Deep Learning Design",
        "authors": "David Neural, Elena Search, Frank Architecture",
        "abstract": "Manual design of neural network architectures is time-consuming and often suboptimal. Neural Architecture Search (NAS) automates this process by searching through the space of possible architectures. This survey examines recent advances in NAS methodologies, efficiency improvements, and applications across computer vision and natural language processing.",
        "categories": "cs.LG, cs.CV, cs.AI",
        "published_date": "2024-12-05T16:45:12Z",
        "arxiv_id": "2412.05432",
        "pdf_url": "https://arxiv.org/pdf/2412.05432.pdf"
    },
    {
        "id": 7,
        "title": "Federated Learning: Privacy-Preserving Machine Learning",
        "authors": "Grace Federated, Henry Privacy, Iris Distributed",
        "abstract": "Federated learning enables training machine learning models across decentralized data sources without centralizing sensitive data. This paper reviews federated learning algorithms, privacy guarantees, and challenges in heterogeneous environments. We discuss applications in healthcare, finance, and mobile computing.",
        "categories": "cs.LG, cs.CR, cs.DC",
        "published_date": "2024-12-03T11:20:33Z",
        "arxiv_id": "2412.03211",
        "pdf_url": "https://arxiv.org/pdf/2412.03211.pdf"
    },
    {
        "id": 8,
        "title": "Multimodal Learning: Integrating Vision, Language, and Audio",
        "authors": "Jack Multimodal, Kelly Vision, Liam Audio",
        "abstract": "Recent advances in multimodal learning have enabled AI systems to process and understand multiple types of data simultaneously. This comprehensive review covers vision-language models, audio-visual learning, and cross-modal retrieval. We analyze architectural innovations and benchmark performance across diverse multimodal tasks.",
        "categories": "cs.CV, cs.CL, cs.MM",
        "published_date": "2024-12-01T08:15:22Z",
        "arxiv_id": "2412.01888",
        "pdf_url": "https://arxiv.org/pdf/2412.01888.pdf"
    }
]

MOCK_RECOMMENDATIONS = [
    {
        "paper": MOCK_PAPERS[0],  # Attention Is All You Need
        "predicted_rating": 4.8
    },
    {
        "paper": MOCK_PAPERS[1],  # BERT
        "predicted_rating": 4.6
    },
    {
        "paper": MOCK_PAPERS[3],  # GPT paper
        "predicted_rating": 4.2
    },
    {
        "paper": MOCK_PAPERS[5],  # Neural Architecture Search
        "predicted_rating": 4.0
    },
    {
        "paper": MOCK_PAPERS[7],  # Multimodal Learning
        "predicted_rating": 3.9
    }
]

# Main content area functions
def get_all_papers():
    return MOCK_PAPERS

def get_recommendations():
    return MOCK_RECOMMENDATIONS

def rate_paper(paper_id, rating):
    st.success("🎉 Paper rated successfully! (Demo mode)")

def format_categories(categories_str):
    """Format categories as badges"""
    categories = categories_str.split(', ')
    badges_html = ""
    for category in categories:
        badges_html += f'<span class="paper-categories">{category}</span>'
    return badges_html

def create_rating_progress_circle(rating, max_rating=5):
    """Create a circular progress indicator for ratings"""
    percentage = (rating / max_rating) * 100
    circumference = 2 * 3.14159 * 54  # radius = 54
    stroke_dasharray = circumference
    stroke_dashoffset = circumference - (percentage / 100) * circumference
    
    color = "#10b981" if rating >= 4 else "#f59e0b" if rating >= 3 else "#ef4444"
    
    return f"""
    <div class="progress-ring">
        <svg class="progress-ring" width="120" height="120">
            <circle cx="60" cy="60" r="54" stroke="#e5e7eb" stroke-width="6" fill="none"/>
            <circle cx="60" cy="60" r="54" stroke="{color}" stroke-width="6" 
                    fill="none" stroke-dasharray="{stroke_dasharray}" 
                    stroke-dashoffset="{stroke_dashoffset}"/>
        </svg>
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); 
                    font-weight: 700; font-size: 1.2rem; color: {color};">
            {rating:.1f}/5
        </div>
    </div>
    """

def render_paper_card(paper, predicted_rating=None, paper_index=0):
    """Render a beautiful paper card using native Streamlit components"""
    
    # Create a container with custom styling
    with st.container():
        # Add a simple visual separator for the paper card
        st.markdown("""
        <div style="
            height: 2px;
            background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
            margin: 1rem 0 0.5rem 0;
            border-radius: 1px;
        "></div>
        """, unsafe_allow_html=True)
        
        # Title
        st.markdown(f"""
        <div style="
            font-size: 1.3rem;
            font-weight: 600;
            color: #1f2937;
            margin-bottom: 0.8rem;
            line-height: 1.5;
        ">
            {paper['title']}
        </div>
        """, unsafe_allow_html=True)
        
        # Authors
        st.markdown(f"""
        <div style="
            color: #667eea;
            font-weight: 500;
            margin-bottom: 0.8rem;
        ">
            👥 {paper['authors']}
        </div>
        """, unsafe_allow_html=True)
        
        # Categories as individual components
        categories = paper['categories'].split(', ')
        if categories:
            cols = st.columns(min(len(categories), 6))  # Max 6 categories per row
            for i, category in enumerate(categories[:6]):  # Show max 6 categories
                with cols[i % len(cols)]:
                    st.markdown(f"""
                    <div style="
                        background: linear-gradient(135deg, #f3f4f6, #e5e7eb);
                        color: #374151;
                        padding: 0.3rem 0.6rem;
                        border-radius: 20px;
                        font-size: 0.75rem;
                        text-align: center;
                        margin: 0.2rem;
                        font-weight: 500;
                        border: 1px solid rgba(255, 255, 255, 0.5);
                    ">
                        {category}
                    </div>
                    """, unsafe_allow_html=True)
        
        # Publication date
        st.markdown(f"""
        <div style="
            color: #9ca3af;
            font-size: 0.9rem;
            margin: 0.8rem 0;
        ">
            📅 Published: {paper['published_date'][:10]}
        </div>
        """, unsafe_allow_html=True)
        
        # Predicted rating badge (if available)
        if predicted_rating:
            st.markdown(f"""
            <div style="
                display: inline-block;
                background: linear-gradient(135deg, #10b981, #059669);
                color: white;
                padding: 0.6rem 1.2rem;
                border-radius: 30px;
                font-weight: 600;
                font-size: 0.9rem;
                margin-bottom: 1rem;
                box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
            ">
                ⭐ Predicted Rating: {predicted_rating:.1f}/5
            </div>
            """, unsafe_allow_html=True)
        
        # Abstract as clean Streamlit text
        st.markdown("**Abstract:**")
        abstract_text = paper['abstract'][:300] + ('...' if len(paper['abstract']) > 300 else '')
        st.markdown(f"""
        <div style="
            color: #4b5563;
            line-height: 1.7;
            margin-bottom: 1.5rem;
            font-size: 0.95rem;
            padding: 1rem;
            background: rgba(249, 250, 251, 0.5);
            border-radius: 8px;
            border-left: 3px solid #667eea;
        ">
            {abstract_text}
        </div>
        """, unsafe_allow_html=True)
        
        # Buttons and rating in columns
        col1, col2, col3 = st.columns([2, 2, 3])
        
        with col1:
            st.link_button("📄 View PDF", paper['pdf_url'], help="Open PDF in new tab")
        
        with col2:
            # Extract the arXiv ID from the full URL if needed
            arxiv_id = paper['arxiv_id']
            
            # Handle cases where arxiv_id might be a full URL
            if 'arxiv.org/abs/' in arxiv_id:
                # Extract just the ID part after '/abs/'
                arxiv_id = arxiv_id.split('/abs/')[-1]
            elif arxiv_id.startswith('http'):
                # Handle other URL formats
                arxiv_id = arxiv_id.split('/')[-1]
            
            # Remove version number if present (e.g., v1, v2)
            if 'v' in arxiv_id and arxiv_id.split('v')[-1].isdigit():
                arxiv_id = arxiv_id.split('v')[0]
            
            # Construct the proper arXiv URL
            arxiv_url = f"https://arxiv.org/abs/{arxiv_id}"
            
            # Use st.link_button for reliable external links
            st.link_button("🔗 arXiv Link", arxiv_url, help="View on arXiv (opens in new tab)")
        
        with col3:
            st.markdown("**Rate this paper:**")
            user_rating = st.slider(
                "Your rating",
                min_value=1,
                max_value=5,
                value=int(predicted_rating) if predicted_rating else 3,
                key=f"rating_{paper['id']}_{paper_index}",
                help="Rate from 1 (poor) to 5 (excellent)"
            )
            
            if st.button("⭐ Submit Rating", key=f"submit_{paper['id']}_{paper_index}"):
                rate_paper(paper['id'], user_rating)

def filter_papers_by_date(papers, date_filter):
    """Filter papers by date range"""
    if date_filter == "All time":
        return papers
    
    from datetime import datetime, timedelta
    now = datetime.now()
    
    if date_filter == "Last 7 days":
        cutoff = now - timedelta(days=7)
    elif date_filter == "Last 30 days":
        cutoff = now - timedelta(days=30)
    elif date_filter == "Last 90 days":
        cutoff = now - timedelta(days=90)
    elif date_filter == "Last year":
        cutoff = now - timedelta(days=365)
    else:
        return papers
    
    filtered = []
    for paper in papers:
        try:
            paper_date = datetime.fromisoformat(paper['published_date'].replace('Z', '+00:00'))
            if paper_date.replace(tzinfo=None) >= cutoff:
                filtered.append(paper)
        except:
            # If date parsing fails, include the paper
            filtered.append(paper)
    
    return filtered

def filter_papers_by_categories(papers, selected_categories):
    """Filter papers by selected categories"""
    if not selected_categories:
        return papers
    
    filtered = []
    for paper in papers:
        paper_categories = paper['categories'].split(', ')
        if any(cat in selected_categories for cat in paper_categories):
            filtered.append(paper)
    
    return filtered

# Page configuration
st.set_page_config(
    page_title="arXiv Paper Recommender - Demo",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        font-size: 3.5rem;
        font-weight: 700;
        color: #000000;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 
            0 1px 0 rgba(255,255,255,0.8),
            0 2px 4px rgba(102, 126, 234, 0.3),
            0 4px 8px rgba(118, 75, 162, 0.2),
            0 8px 16px rgba(240, 147, 251, 0.15);
        animation: fadeInDown 1s ease-out;
        position: relative;
    }
    
    .subtitle {
        font-size: 1.3rem;
        color: #6b7280;
        text-align: center;
        margin-bottom: 3rem;
        font-weight: 400;
        animation: fadeInUp 1s ease-out 0.2s both;
    }
    
    .paper-categories {
        display: inline-block;
        background: linear-gradient(135deg, #f3f4f6, #e5e7eb);
        color: #374151;
        padding: 0.4rem 0.8rem;
        border-radius: 25px;
        font-size: 0.8rem;
        margin: 0.25rem 0.25rem 0.8rem 0;
        font-weight: 500;
        border: 1px solid rgba(255, 255, 255, 0.5);
        transition: all 0.3s ease;
    }
    
    .paper-categories:hover {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        transform: scale(1.05);
    }
    
    .rating-badge {
        display: inline-block;
        background: linear-gradient(135deg, #10b981, #059669);
        color: white;
        padding: 0.6rem 1.2rem;
        border-radius: 30px;
        font-weight: 600;
        font-size: 0.9rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    .stats-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
        padding: 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        border-radius: 20px;
        color: white;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
        position: relative;
        overflow: hidden;
    }
    
    .stats-container::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
        animation: shimmer 3s infinite;
    }
    
    @keyframes shimmer {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
        100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
    }
    
    .stat-item {
        text-align: center;
        position: relative;
        z-index: 1;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        display: block;
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    
    .stat-label {
        font-size: 0.95rem;
        opacity: 0.9;
        font-weight: 500;
    }
    
    .section-header {
        font-size: 1.8rem;
        font-weight: 600;
        color: #1f2937;
        margin: 2.5rem 0 1.5rem 0;
        padding: 1rem 0;
        border-bottom: 3px solid transparent;
        background: linear-gradient(white, white) padding-box,
                    linear-gradient(90deg, #667eea, #764ba2) border-box;
        border-bottom: 3px solid;
        border-image: linear-gradient(90deg, #667eea, #764ba2) 1;
        position: relative;
    }
    
    .progress-ring {
        width: 120px;
        height: 120px;
        position: relative;
        margin: 0 auto 1rem;
    }
    
    .progress-ring circle {
        fill: none;
        stroke-width: 6;
        stroke-linecap: round;
        transform: rotate(-90deg);
        transform-origin: 50% 50%;
        transition: stroke-dasharray 0.5s ease;
    }
    
    .floating-action {
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        width: 60px;
        height: 60px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 1.5rem;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        cursor: pointer;
        transition: all 0.3s ease;
        z-index: 1000;
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .floating-action:hover {
        transform: scale(1.1) translateY(-5px);
        box-shadow: 0 12px 35px rgba(102, 126, 234, 0.6);
    }
    
    /* Animations */
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 0.6rem 1.5rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4) !important;
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #5a6fd8, #6b47a0);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">📚 arXiv Paper Recommender</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Discover and explore the latest research papers with AI-powered recommendations</p>', unsafe_allow_html=True)

# Add deployment notice banner
st.markdown("""
<div style="
    background: linear-gradient(135deg, #fef3c7, #fbbf24);
    color: #92400e;
    padding: 1rem 1.5rem;
    border-radius: 12px;
    margin: 1rem 0 2rem 0;
    border: 1px solid #f59e0b;
    text-align: center;
    font-weight: 500;
    box-shadow: 0 4px 12px rgba(251, 191, 36, 0.3);
">
    🚀 <strong>Demo Mode:</strong> You're viewing a demonstration version with sample data. 
    In production, this would connect to a live arXiv API and recommendation engine.
</div>
""", unsafe_allow_html=True)

# Add floating back-to-top button
st.markdown("""
<div class="floating-action" onclick="window.scrollTo({top: 0, behavior: 'smooth'});" title="Back to top">
    ⬆️
</div>
""", unsafe_allow_html=True)

# Sidebar with beautiful styling
with st.sidebar:
    st.markdown("### 🎯 Quick Actions")
    
    if st.button("🔄 Fetch Daily Papers", key="fetch_btn", help="Fetch the latest papers from arXiv"):
        with st.spinner("Fetching papers from arXiv..."):
            st.success("✅ Successfully fetched daily papers! (Demo mode - using sample data)")
    
    st.markdown("---")
    st.markdown("### 📊 Filter Options")
    
    # Add category filter in sidebar
    all_papers_for_filter = get_all_papers()
    if all_papers_for_filter:
        all_categories = set()
        for paper in all_papers_for_filter:
            categories = paper['categories'].split(', ')
            all_categories.update(categories)
        
        selected_categories = st.multiselect(
            "🏷️ Filter by categories",
            options=sorted(list(all_categories)),
            help="Select categories to filter papers"
        )
        
        # Add date range filter
        st.markdown("📅 **Publication Date Range**")
        date_filter = st.selectbox(
            "Select time range",
            ["All time", "Last 7 days", "Last 30 days", "Last 90 days", "Last year"]
        )

# Display options with beautiful styling
display_option = st.radio(
    "**Choose what to display:**",
    ["All Papers", "Personalized Recommendations"],
    index=0,
    help="All Papers shows everything in the database, Recommendations shows papers tailored to your preferences"
)

if display_option == "All Papers":
    # Get all papers
    all_papers = get_all_papers()
    
    if not all_papers:
        st.info("📭 No papers available. Try fetching daily papers from the sidebar!")
    else:
        # Apply filters
        filtered_papers = all_papers
        
        # Apply category filter if selected
        if 'selected_categories' in locals() and selected_categories:
            filtered_papers = filter_papers_by_categories(filtered_papers, selected_categories)
        
        # Apply date filter if selected
        if 'date_filter' in locals():
            filtered_papers = filter_papers_by_date(filtered_papers, date_filter)
        
        # Enhanced stats section with more metrics
        total_papers = len(filtered_papers)
        total_categories = len(set(paper['categories'] for paper in filtered_papers))
        total_authors = len(set(paper['authors'] for paper in filtered_papers))
        avg_abstract_length = sum(len(paper['abstract']) for paper in filtered_papers) / len(filtered_papers) if filtered_papers else 0
        
        st.markdown(f"""
        <div class="stats-container">
            <div class="stat-item">
                <span class="stat-number">{total_papers}</span>
                <span class="stat-label">Total Papers</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">{total_categories}</span>
                <span class="stat-label">Categories</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">{total_authors}</span>
                <span class="stat-label">Unique Authors</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">{int(avg_abstract_length)}</span>
                <span class="stat-label">Avg Abstract Length</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Category distribution visualization
        if filtered_papers:
            st.markdown('<h3 class="section-header">🏷️ Category Distribution</h3>', unsafe_allow_html=True)
            
            # Create category distribution
            category_counts = {}
            for paper in filtered_papers:
                categories = paper['categories'].split(', ')
                for category in categories:
                    category_counts[category] = category_counts.get(category, 0) + 1
            
            # Sort by count and take top 10
            top_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)[:10]
            
            if top_categories:
                # Display as Streamlit columns for better compatibility
                cols_per_row = 5
                rows = [top_categories[i:i + cols_per_row] for i in range(0, len(top_categories), cols_per_row)]
                
                for row in rows:
                    cols = st.columns(len(row))
                    for col, (category, count) in zip(cols, row):
                        with col:
                            # Create a styled metric display
                            st.markdown(f"""
                            <div style="
                                background: linear-gradient(135deg, #e0e7ff, #c7d2fe);
                                color: #3730a3;
                                padding: 0.5rem 1rem;
                                border-radius: 20px;
                                text-align: center;
                                margin: 0.25rem;
                                font-weight: 500;
                                transition: all 0.3s ease;
                                cursor: pointer;
                                border: 1px solid rgba(255, 255, 255, 0.3);
                                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                            ">
                                <div style="font-size: 0.9rem; font-weight: 600;">{category}</div>
                                <div style="font-size: 0.75rem; opacity: 0.8;">{count} papers</div>
                            </div>
                            """, unsafe_allow_html=True)
        
        st.markdown(f'<h2 class="section-header">📚 All Papers ({total_papers} papers)</h2>', unsafe_allow_html=True)
        
        # Enhanced search and filter options
        col1, col2 = st.columns([3, 1])
        with col1:
            search_term = st.text_input("🔍 Search papers", placeholder="Search by title, authors, or abstract...")
        with col2:
            sort_option = st.selectbox("📊 Sort by", ["Published Date (Newest)", "Published Date (Oldest)", "Title A-Z"])
        
        # Filter papers based on search
        if search_term:
            filtered_papers = [
                paper for paper in filtered_papers
                if search_term.lower() in paper['title'].lower() or 
                   search_term.lower() in paper['authors'].lower() or
                   search_term.lower() in paper['abstract'].lower()
            ]
        
        # Sort papers
        if sort_option == "Published Date (Newest)":
            filtered_papers.sort(key=lambda x: x['published_date'], reverse=True)
        elif sort_option == "Published Date (Oldest)":
            filtered_papers.sort(key=lambda x: x['published_date'])
        elif sort_option == "Title A-Z":
            filtered_papers.sort(key=lambda x: x['title'])
        
        if filtered_papers:
            if search_term or (selected_categories if 'selected_categories' in locals() else False):
                st.info(f"📄 Showing {len(filtered_papers)} papers matching your filters")
            else:
                st.info(f"📄 Showing {len(filtered_papers)} papers")
            
            # Display papers with enhanced visuals
            for i, paper in enumerate(filtered_papers):
                render_paper_card(paper, paper_index=i)
        else:
            st.warning("🔍 No papers found matching your search criteria.")

else:
    # Get recommendations
    recommendations = get_recommendations()

    if not recommendations:
        st.info("🎯 No recommendations available yet. Rate some papers first to get personalized recommendations!")
        
        # Show some recent papers to get started
        recent_papers = get_all_papers()[:5]  # Get 5 recent papers
        if recent_papers:
            st.markdown('<h3 class="section-header">🚀 Get Started - Rate These Papers</h3>', unsafe_allow_html=True)
            for i, paper in enumerate(recent_papers):
                render_paper_card(paper, paper_index=f"starter_{i}")
    else:
        # Enhanced stats for recommendations
        total_recs = len(recommendations)
        max_rating = max(rec['predicted_rating'] for rec in recommendations)
        avg_rating = sum(rec['predicted_rating'] for rec in recommendations) / len(recommendations)
        min_rating = min(rec['predicted_rating'] for rec in recommendations)
        
        # Create a visual rating distribution
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### Top Rating")
            st.markdown(create_rating_progress_circle(max_rating), unsafe_allow_html=True)
        
        with col2:
            st.markdown("### Average Rating")
            st.markdown(create_rating_progress_circle(avg_rating), unsafe_allow_html=True)
        
        with col3:
            st.markdown("### Rating Range")
            st.markdown(f"""
            <div style="text-align: center; padding: 2rem;">
                <div style="font-size: 1.5rem; font-weight: 600; color: #667eea;">
                    {min_rating:.1f} - {max_rating:.1f}
                </div>
                <div style="color: #6b7280; margin-top: 0.5rem;">Rating Spread</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown(f'<h2 class="section-header">🎯 Your Personalized Recommendations ({total_recs} papers)</h2>', unsafe_allow_html=True)
        
        # Display each recommendation with enhanced visuals
        for i, recommendation in enumerate(recommendations):
            paper = recommendation['paper']
            predicted_rating = recommendation['predicted_rating']
            render_paper_card(paper, predicted_rating, paper_index=f"rec_{i}")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6b7280; padding: 2rem 0;">
    <p>© 2024 arXiv Paper Recommender | Powered by AI & Machine Learning</p>
    <p>🔬 Discover • 📖 Learn • 🚀 Innovate</p>
    <p><strong>Demo Version:</strong> Sample data for demonstration purposes</p>
</div>
""", unsafe_allow_html=True) 