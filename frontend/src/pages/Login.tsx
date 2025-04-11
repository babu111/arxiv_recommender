import React, { useState } from 'react';
import {
    Container,
    Box,
    Typography,
    TextField,
    Button,
    Paper,
    Link,
} from '@mui/material';
import { useNavigate } from 'react-router-dom';
import { auth } from '../services/api';

const Login: React.FC = () => {
    const navigate = useNavigate();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState<string | null>(null);
    const [isRegistering, setIsRegistering] = useState(false);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setError(null);

        try {
            const response = isRegistering
                ? await auth.register(email, password)
                : await auth.login(email, password);

            localStorage.setItem('token', response.access_token);
            navigate('/');
        } catch (err) {
            setError(isRegistering
                ? 'Failed to register. Please try again.'
                : 'Invalid email or password.');
            console.error(err);
        }
    };

    return (
        <Container maxWidth="sm">
            <Box
                sx={{
                    marginTop: 8,
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                }}
            >
                <Paper elevation={3} sx={{ p: 4, width: '100%' }}>
                    <Typography component="h1" variant="h5" align="center" gutterBottom>
                        {isRegistering ? 'Register' : 'Sign In'}
                    </Typography>

                    {error && (
                        <Typography color="error" align="center" gutterBottom>
                            {error}
                        </Typography>
                    )}

                    <Box component="form" onSubmit={handleSubmit} sx={{ mt: 1 }}>
                        <TextField
                            margin="normal"
                            required
                            fullWidth
                            id="email"
                            label="Email Address"
                            name="email"
                            autoComplete="email"
                            autoFocus
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                        />
                        <TextField
                            margin="normal"
                            required
                            fullWidth
                            name="password"
                            label="Password"
                            type="password"
                            id="password"
                            autoComplete="current-password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                        <Button
                            type="submit"
                            fullWidth
                            variant="contained"
                            sx={{ mt: 3, mb: 2 }}
                        >
                            {isRegistering ? 'Register' : 'Sign In'}
                        </Button>
                        <Box textAlign="center">
                            <Link
                                component="button"
                                variant="body2"
                                onClick={() => setIsRegistering(!isRegistering)}
                            >
                                {isRegistering
                                    ? 'Already have an account? Sign in'
                                    : "Don't have an account? Register"}
                            </Link>
                        </Box>
                    </Box>
                </Paper>
            </Box>
        </Container>
    );
};

export default Login; 