import axios, {AxiosInstance} from "axios"

const api: AxiosInstance = axios.create({
    // baseURL: process.env.NEXT_PUBLIC_SERVER,
 });
  
export default api;