"use client";

import Breadcrumb from "@/components/Common/Breadcrumb";
import { columns } from "@/components/Stocks/columns";
import { DataTable } from "@/components/Stocks/data-table";
import ScreenerPage from "@/components/Stocks/screener";
import useDataTableHooks from "@/hooks/useDataTableHooks";
import StocksDataService from "@/services/stocksDataService";
import { useQuery } from "@tanstack/react-query";

const Stocks = () => {
  const stockDataPageHook = useDataTableHooks({
    queryFetch: useQuery({
      queryKey: ["stocks"],
      queryFn: async () => {
        return await StocksDataService.getListedStocks(
          stockDataPageHook.columnFiltersObject,
          stockDataPageHook.currentPage,
          stockDataPageHook.itemPerRow,
        );
      },
    }),
  });
  return (
    <>
      <section className="pb-[120px] pt-[120px]">
        <div className="container">
          <div className="-mx-4 my-12 flex flex-wrap justify-center">
            <div className="mx-4 my-12">
            {/* <ScreenerPage {...stockDataPageHook} /> */}
            </div>
            {!stockDataPageHook.queryFetch.isLoading && (
              <DataTable
                columns={columns}
                stockDataPageHook={stockDataPageHook}
              />
            )}
          </div>

          <div className="-mx-4 flex flex-wrap" data-wow-delay=".15s">
            <div className="w-full px-4">
              <ul className="flex items-center justify-center pt-8">
                <li className="mx-1">
                  <a
                    href="#0"
                    className="flex h-9 min-w-[36px] items-center justify-center rounded-md bg-body-color bg-opacity-[15%] px-4 text-sm text-body-color transition hover:bg-primary hover:bg-opacity-100 hover:text-white"
                  >
                    Prev
                  </a>
                </li>
                <li className="mx-1">
                  <a
                    href="#0"
                    className="flex h-9 min-w-[36px] items-center justify-center rounded-md bg-body-color bg-opacity-[15%] px-4 text-sm text-body-color transition hover:bg-primary hover:bg-opacity-100 hover:text-white"
                  >
                    1
                  </a>
                </li>
                <li className="mx-1">
                  <a
                    href="#0"
                    className="flex h-9 min-w-[36px] items-center justify-center rounded-md bg-body-color bg-opacity-[15%] px-4 text-sm text-body-color transition hover:bg-primary hover:bg-opacity-100 hover:text-white"
                  >
                    2
                  </a>
                </li>
                <li className="mx-1">
                  <a
                    href="#0"
                    className="flex h-9 min-w-[36px] items-center justify-center rounded-md bg-body-color bg-opacity-[15%] px-4 text-sm text-body-color transition hover:bg-primary hover:bg-opacity-100 hover:text-white"
                  >
                    3
                  </a>
                </li>
                <li className="mx-1">
                  <span className="flex h-9 min-w-[36px] cursor-not-allowed items-center justify-center rounded-md bg-body-color bg-opacity-[15%] px-4 text-sm text-body-color">
                    ...
                  </span>
                </li>
                <li className="mx-1">
                  <a
                    href="#0"
                    className="flex h-9 min-w-[36px] items-center justify-center rounded-md bg-body-color bg-opacity-[15%] px-4 text-sm text-body-color transition hover:bg-primary hover:bg-opacity-100 hover:text-white"
                  >
                    12
                  </a>
                </li>
                <li className="mx-1">
                  <a
                    href="#0"
                    className="flex h-9 min-w-[36px] items-center justify-center rounded-md bg-body-color bg-opacity-[15%] px-4 text-sm text-body-color transition hover:bg-primary hover:bg-opacity-100 hover:text-white"
                  >
                    Next
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default Stocks;
