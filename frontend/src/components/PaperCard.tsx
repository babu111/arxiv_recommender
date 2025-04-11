import React from 'react';
import {
    Card,
    CardContent,
    CardActions,
    Typography,
    Button,
    Rating,
    Box,
} from '@mui/material';
import { Paper } from '../types';

interface PaperCardProps {
    paper: Paper;
    onRate?: (rating: number) => void;
    userRating?: number;
}

const PaperCard: React.FC<PaperCardProps> = ({ paper, onRate, userRating }) => {
    return (
        <Card sx={{ mb: 2, maxWidth: '100%' }}>
            <CardContent>
                <Typography variant="h5" component="div" gutterBottom>
                    {paper.title}
                </Typography>
                <Typography variant="subtitle1" color="text.secondary" gutterBottom>
                    {paper.authors}
                </Typography>
                <Typography variant="body2" color="text.secondary" paragraph>
                    {paper.abstract}
                </Typography>
                <Typography variant="caption" color="text.secondary">
                    Categories: {paper.categories}
                </Typography>
            </CardContent>
            <CardActions>
                <Button
                    size="small"
                    color="primary"
                    href={paper.pdf_url}
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    View PDF
                </Button>
                {onRate && (
                    <Box sx={{ ml: 'auto' }}>
                        <Rating
                            value={userRating || 0}
                            onChange={(_, value) => value && onRate(value)}
                            precision={1}
                        />
                    </Box>
                )}
            </CardActions>
        </Card>
    );
};

export default PaperCard; 