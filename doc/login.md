
To disable the authentication requirements and bypass the login/registration flow, you'll need to make a few modifications. Here's how to do it:

1. First, let's modify the `App.tsx` file to bypass the authentication check:

```typescript jsx:frontend/src/App.tsx
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
            element={<Home />}
          />
          <Route
            path="/login"
            element={<Navigate to="/" replace />}
          />
        </Routes>
      </Router>
    </ThemeProvider>
  );
};

export default App;
```
2. Now we need to make sure the API requests don't fail due to missing authentication. Let's modify the API interceptor to add a mock token:

```typescript:frontend/src/services/api.ts
import axios from 'axios';
import { Paper, User, UserPreference, ReadingHistory, Recommendation } from '../types';

const API_URL = 'http://localhost:8000';

const api = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

// Add mock token to all requests - for development only
api.interceptors.request.use((config) => {
    // Add a mock token for development - bypassing authentication
    config.headers.Authorization = `Bearer mock_development_token`;
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
// ... rest of the file
```
3. Finally, we need to modify the backend to accept our mock token. Let's add a mock user validation in the authentication router:

```python:backend/app/routers/auth.py
// ... existing code ...

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # Development bypass - accept mock token
    if token == "mock_development_token":
        # Return a mock user for development
        return User(
            id=1,
            email="dev@example.com",
            hashed_password="mock_hash",
            is_active=True
        )
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.email == token_data.email).first()
    if user is None:
        raise credentials_exception
    return user

// ... rest of the file ...
```
Now you should be able to bypass the login/registration functionality and directly access the homepage and main features. Here's what these changes do:

1. The `App.tsx` modification always considers the user as authenticated and directly renders the Home component.

2. The `api.ts` modification adds a mock token to every API request instead of checking for a token in localStorage.

3. The `auth.py` modification allows the backend to accept a mock token and return a mock user for API requests that require authentication.

To test these changes:

1. Restart both your frontend and backend servers:

   **Backend**:
   ```bash
   cd backend
   source venv/bin/activate
   uvicorn app.main:app --reload
   ```
   
   **Frontend**:
   ```bash
   cd frontend
   npm start
   ```

2. Open your browser and navigate to `http://localhost:3000` - you should now be automatically redirected to the homepage without having to login.

When you're ready to re-enable authentication later, simply revert these changes:

1. Restore `isAuthenticated = !!localStorage.getItem('token');` in `App.tsx`
2. Revert the token interceptor in `api.ts`
3. Remove the mock token check in `auth.py`

Would you like any additional changes to make the development process easier?
