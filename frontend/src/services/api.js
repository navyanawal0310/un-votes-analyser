import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000",
});

export const getCountry = (country) =>
  API.get(`/country/${country}`);

export const compareCountries = (c1, c2) =>
  API.get(`/compare/${c1}/${c2}`);

export const getGlobalIssue = (issue) =>
  API.get(`/global/${issue}`);