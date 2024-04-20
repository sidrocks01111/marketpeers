// Module for Stocks Data 
import api from "@/client/requests";
import CONSTANTS from "../config/constants";

// Stocks Data Service
class StocksDataService {
  protected static prefix_endpoint = CONSTANTS.PATH.GET_STOCKS_MarketPeer_PATH;

  /**
   * search anomalies
   * @param page_size size of the page
   * @param page current page to get
   * @returns list of stocks and counts
   * ex: {entries: [], total: 0}
   */
  public static getListedStocks = async (
    query: Record<string, any>,
    page: number = 1,
    page_size: number = 10
  ): Promise<any[]> => {
    const res = await api.post(
      `${this.prefix_endpoint}/query`,
      {...query},
      {
        params: {
          page,
          page_size,
        },
      }
    );
    return res.data;
  };
}

export default StocksDataService;