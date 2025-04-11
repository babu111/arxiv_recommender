import React, { useEffect, useState } from 'react';
import {
    Container,
    Typography,
    Box,
    Button,
    CircularProgress,
} from '@mui/material';
import { Paper, Recommendation } from '../types';
import { papers } from '../services/api';
import PaperCard from '../components/PaperCard';

const Home: React.FC = () => {
    const [recommendations, setRecommendations] = useState<Recommendation[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        fetchRecommendations();
    }, []);

    const fetchRecommendations = async () => {
        try {
            setLoading(true);
            // TODO: Replace with actual user ID from auth context
            const userId = 1;
            const data = await papers.getRecommendations(userId);
            setRecommendations(data);
            setError(null);
        } catch (err) {
            setError('Failed to fetch recommendations');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const handleRatePaper = async (paperId: number, rating: number) => {
        try {
            // TODO: Replace with actual user ID from auth context
            const userId = 1;
            await papers.ratePaper(paperId, userId, rating);
            // Refresh recommendations after rating
            fetchRecommendations();
        } catch (err) {
            console.error('Failed to rate paper:', err);
        }
    };

    const handleFetchDaily = async () => {
        try {
            await papers.fetchDaily();
            fetchRecommendations();
        } catch (err) {
            console.error('Failed to fetch daily papers:', err);
        }
    };

    if (loading) {
        return (
            <Box display="flex" justifyContent="center" alignItems="center" minHeight="80vh">
                <CircularProgress />
            </Box>
        );
    }

    return (
        <Container maxWidth="lg" sx={{ py: 4 }}>
            <Box display="flex" justifyContent="space-between" alignItems="center" mb={4}>
                <Typography variant="h4" component="h1">
                    Recommended Papers
                </Typography>
                <Button variant="contained" onClick={handleFetchDaily}>
                    Fetch Daily Papers
                </Button>
            </Box>

            {error && (
                <Typography color="error" mb={2}>
                    {error}
                </Typography>
            )}

            {recommendations.length === 0 ? (
                <Typography>No recommendations available. Try rating some papers!</Typography>
            ) : (
                recommendations.map((rec) => (
                    <PaperCard
                        key={rec.paper.id}
                        paper={rec.paper}
                        onRate={(rating) => handleRatePaper(rec.paper.id, rating)}
                        userRating={rec.predicted_rating}
                    />
                ))
            )}
        </Container>
    );
};

export default Home; 