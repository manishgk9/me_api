import { configureStore } from "@reduxjs/toolkit";
import searchReducer from "./redux/apiSlice";
const store = configureStore({
  reducer: {
    search: searchReducer,
  },
});

export default store;
