import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { ThemeProvider, createTheme, CssBaseline } from '@mui/material';
import Home from './pages/Home';
import Login from './pages/Login';

const theme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
  },
});

const App: React.FC = () => {
  // Bypass authentication check - always return true for development
  const isAuthenticated = true; // Temporarily disabled auth check

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Routes>
          <Route
            path="/"
            // element={
            //   isAuthenticated ? <Home /> : <Navigate to="/login" replace />
            // }
            element={<Home />}
          />
          <Route
            path="/login"
            // element={
            //   !isAuthenticated ? <Login /> : <Navigate to="/" replace />
            // }
            element={<Navigate to="/" replace />}
          />
        </Routes>
      </Router>
    </ThemeProvider>
  );
};

export default App;
