import { Routes, Route } from "react-router";
import { ThemeProvider, createTheme } from '@mui/material/styles';

const theme = createTheme({
  colorSchemes: {
    dark: false,
  },
});
import routes from "./routes";

function App() {
  return (
    <ThemeProvider theme={theme}>
      <Routes>
        {routes.map((route) => (
          <Route key={route.path} path={route.path} element={<route.element />} />
        ))}
      </Routes>
    </ThemeProvider>
  );
}

export default App;