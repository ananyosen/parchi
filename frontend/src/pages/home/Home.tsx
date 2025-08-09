import React, { useEffect } from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import { alpha, useTheme } from '@mui/material/styles';

const Home: React.FC = () => {
  const theme = useTheme();
  console.log(theme.palette)

  useEffect(() => {
    fetch('/api/assets')
    .then(response => response.json())
    .then(console.log);
  }, []);
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static" sx={{
        backdropFilter: 'blur(10px)',
        backgroundColor: alpha(theme.palette.background.paper, 0.6),
      }}>
        <Toolbar>
          <IconButton
            size="large"
            edge="start"
            color="inherit"
            aria-label="open drawer"
            sx={{ mr: 2 }}
          >
            <img src="/parchi.svg" alt="Parchi Logo" style={{ height: '32px' }} />
          </IconButton>
        </Toolbar>
      </AppBar>
      <Box component="main" sx={{ p: 3 }}>
      </Box>
    </Box>
  )
};

export default Home;
