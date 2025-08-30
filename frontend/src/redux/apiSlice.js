import { createSlice } from "@reduxjs/toolkit";
import { searchProjects, searchUsers } from "../services/api";
const apiSlice = createSlice({
  name: "search",
  initialState: { items: null, loading: false, error: null, mode: "projects" },
  reducers: {
    setMode: (state, action) => {
      state.mode = action.payload;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(searchProjects.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(searchProjects.fulfilled, (state, action) => {
        state.loading = false;
        state.items = action.payload;
      })
      .addCase(searchProjects.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload?.detail || "Error searching projects";
      })
      .addCase(searchUsers.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(searchUsers.fulfilled, (state, action) => {
        state.loading = false;
        state.items = action.payload;
        // console.log(action.payload);
      })
      .addCase(searchUsers.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload?.detail || "Error searching users";
      });
  },
});

export const { setMode } = apiSlice.actions;
export default apiSlice.reducer;
