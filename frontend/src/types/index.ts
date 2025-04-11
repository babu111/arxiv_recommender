export interface Paper {
    id: number;
    arxiv_id: string;
    title: string;
    authors: string;
    abstract: string;
    categories: string;
    published_date: string;
    pdf_url: string;
}

export interface User {
    id: number;
    email: string;
}

export interface UserPreference {
    id: number;
    user_id: number;
    paper_id: number;
    rating: number;
    timestamp: string;
}

export interface ReadingHistory {
    id: number;
    user_id: number;
    paper_id: number;
    read_date: string;
}

export interface Recommendation {
    paper: Paper;
    predicted_rating: number;
} 