import axios from 'axios';
import { Paper, User, UserPreference, ReadingHistory, Recommendation } from '../types';

const API_URL = 'http://localhost:8000';

const api = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

// Add token to requests if it exists
api.interceptors.request.use((config) => {
    const token = localStorage.getItem('token');
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

export const auth = {
    login: async (email: string, password: string) => {
        const response = await api.post('/auth/token', { username: email, password });
        return response.data;
    },
    register: async (email: string, password: string) => {
        const response = await api.post('/auth/register', { email, password });
        return response.data;
    },
};

export const papers = {
    getAll: async (): Promise<Paper[]> => {
        const response = await api.get('/api/papers/');
        return response.data;
    },
    getRecommendations: async (userId: number): Promise<Recommendation[]> => {
        const response = await api.get(`/api/papers/recommendations/${userId}`);
        return response.data;
    },
    ratePaper: async (paperId: number, userId: number, rating: number) => {
        const response = await api.post(`/api/papers/${paperId}/rate`, {
            user_id: userId,
            rating,
        });
        return response.data;
    },
    fetchDaily: async () => {
        const response = await api.post('/api/papers/fetch-daily');
        return response.data;
    },
}; 