"use client";

import { Button } from "@/components/ui/button";
import { ColumnDef, Row } from "@tanstack/react-table";
import { ArrowUpDown, MoreHorizontal } from "lucide-react";

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type stocksDataTable = {
  stock_name: string;
  exchange: string;
};


export const columns: ColumnDef<stocksDataTable>[] = [
  {
    accessorKey: "stock_name",
    header: "Stocks"
  },
  {
    accessorKey: "stock_fin.marketCap",
    header: "Market Cap",
    id: "stock_mcap"
  },
  {
    accessorKey: "stock_fin.price",
    header: ({ column }) => {
      return (
        <Button
          variant="ghost"
          onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
        >
          Price
          <ArrowUpDown className="ml-2 h-4 w-4" />
        </Button>
      );
    },
  },
  {
    accessorKey: "stock_fin.volume",
    header: ({ column }) => {
      return (
        <Button
          variant="ghost"
          onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
        >
          Volume
          <ArrowUpDown className="ml-2 h-4 w-4" />
        </Button>
      );
    },
  },
  {
    accessorKey: "exchange",
    header: "Exchange",
  },
];
