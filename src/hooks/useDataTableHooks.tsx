
import React, { useEffect, useState, useMemo, Dispatch, SetStateAction } from "react";
import { ColumnFiltersState } from "@tanstack/react-table";
import { UseQueryResult } from "@tanstack/react-query";

interface useDataTableHooksProps {
  queryFetch: UseQueryResult<Record<string, any>>;
  contextQuery?: Record<string, any>;
  refetchCondition?: boolean;
}

interface customColumnFilterState {
  id: string,
  query: any
}

export interface useDataTableHooksReturn {
  queryFetch: UseQueryResult<Record<string, any>>;
  itemPerRow: number;
  setItemPerRow: React.Dispatch<React.SetStateAction<number>>;
  currentPage: number;
  setCurrentPage: React.Dispatch<React.SetStateAction<number>>;
  columnFilters: customColumnFilterState[];
  setColumnFilters: React.Dispatch<React.SetStateAction<customColumnFilterState[]>>;
  columnFiltersObject: Record<string, any>; // replace 'any' with the actual type
  data: any[]; // replace 'any' with the actual type of entries
  totalData: number;
}


function useDataTableHooks({
  queryFetch,
  contextQuery,
  refetchCondition = true,
}: useDataTableHooksProps) {

  const [itemPerRow, setItemPerRow] = useState<number>(10);
  const [currentPage, setCurrentPage] = useState<number>(1);

  // const [columnFilters, setColumnFilters] = useState<customColumnFilterState>(
  //   Object.entries(true).map(([k, v]) => ({
  //     id: k,
  //     query: v,
  //   }))
  // );
  const [columnFilters, setColumnFilters] = useState<customColumnFilterState[]>([])
  /**
   * This useEffect listens for changes in router.isReady, router.query,
   * currentPage, and refetchCondition to trigger a data refetch, providing
   * a new result based on the set filter.
   */
  useEffect(() => {
    if (refetchCondition) {
      queryFetch.refetch();
    }
  }, [currentPage, refetchCondition, itemPerRow, columnFilters]);

  const queryFetchData = useMemo(() => {
    if (queryFetch.data) {
      return queryFetch.data;
    }
    return {
      entries: [],
      total: 0,
    };
  }, [itemPerRow, currentPage, queryFetch]);

  const columnFiltersObject: Record<string, any> = useMemo(
    () =>
      columnFilters.reduce((prev, curr) => {
        return { ...prev, [curr.id]: curr.query };
      }, {}),
    [columnFilters]
  );

  return {
    queryFetch,
    itemPerRow,
    setItemPerRow,
    currentPage,
    setCurrentPage,
    columnFilters,
    setColumnFilters,
    columnFiltersObject,
    data: queryFetchData.entries,
    totalData: queryFetchData.total,
  };
}

export default useDataTableHooks;