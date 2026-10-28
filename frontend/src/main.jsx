import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Dashboard from './pages/Dashboard.jsx';
import Profile from './pages/Profile.jsx';
import Applications from './pages/Applications.jsx';
import MagicConfirm from './pages/MagicConfirm.jsx';
import Layout from './components/Layout.jsx';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Navigate to="/dashboard" replace />} />
          <Route path="dashboard"    element={<Dashboard />} />
          <Route path="profile"      element={<Profile />} />
          <Route path="applications" element={<Applications />} />
        </Route>
        <Route path="/magic-confirm" element={<MagicConfirm />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
