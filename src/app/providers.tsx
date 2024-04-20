"use client";

import React, { useState } from "react"
import { ReactQueryStreamedHydration } from "@tanstack/react-query-next-experimental"
import { QueryClientProvider, QueryClient } from "@tanstack/react-query"
import { ReactQueryDevtools } from "@tanstack/react-query-devtools"
import { ThemeProvider } from "next-themes";

export function Providers({ children }: { children: React.ReactNode }) {
  const [client] = useState(new QueryClient())
  return (
    <ThemeProvider attribute="class" enableSystem={false} defaultTheme="dark">
      <QueryClientProvider client={client}>
        <ReactQueryStreamedHydration>
          {children}
        </ReactQueryStreamedHydration>
        <ReactQueryDevtools initialIsOpen={false} />
      </QueryClientProvider>
    </ThemeProvider>
  );
}
