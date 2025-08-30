import { createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";
const API_BASE_URL =
  import.meta?.env?.FRONTEND_BASE_URL || "http://127.0.0.1:8000/api";

export const api = axios.create({
  baseURL: API_BASE_URL,
  headers: { "Content-Type": "application/json" },
});

export const searchProjects = createAsyncThunk(
  "search/projects",
  async (skillQuery, { rejectWithValue }) => {
    try {
      const { data } = await api.get("/projects/", {
        params: { skill: skillQuery },
      });
      return Array.isArray(data) ? data : data?.results || [];
    } catch (err) {
      return rejectWithValue(
        err.response?.data || { detail: "Failed to load projects" }
      );
    }
  }
);

export const searchUsers = createAsyncThunk(
  "search/users",
  async (searchQuery, { rejectWithValue }) => {
    try {
      const { data } = await api.get("/profiles/", {
        params: { search: searchQuery },
      });
      return Array.isArray(data) ? data : data?.results || [];
    } catch (err) {
      return rejectWithValue(
        err.response?.data || { detail: "Failed to load users" }
      );
    }
  }
);
