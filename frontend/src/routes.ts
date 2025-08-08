import React  from "react";

type RouteType = {
  path: string;
  element: React.FC;
};

const Home = React.lazy(() => import("./pages/home"));
const NotFound = React.lazy(() => import("./pages/404"));

const routes: RouteType[] = [
  { path: "/", element: Home },
  { path: "*", element: NotFound },
];

export default routes;
