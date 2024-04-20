"use client";

import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { Button } from "@/components/ui/button";

import {
  Sheet,
  SheetContent,
  SheetFooter,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet";

import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";

import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

import { Slider } from "@/components/ui/slider"

import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { CustomFilter } from "./customFilter";

import { useDataTableHooksReturn } from '../../hooks/useDataTableHooks';
import { useState } from "react";
import { Input } from "../ui/input";
import React from "react";

const screenerFormSchema = z.object({
  stock_index: z.string().min(2).max(50),
  stock_mcap: z.enum(["Large", "Mid", "Small"]),
});

export default function ScreenerPage(stockDataPageHook: useDataTableHooksReturn) {

  const [popOverFilters, setpopOverFilters] = useState<string[]>([]);

  const form = useForm<z.infer<typeof screenerFormSchema>>({
    resolver: zodResolver(screenerFormSchema),
  });

  const marketCapRadiohandle = (value: string) => {
    let data = 100
    console.log("radio")


    stockDataPageHook.setColumnFilters([{
      id: "stock_fin.marketCap",
      query: {
        "$gte": 10000000
      }
    }])
    console.log(stockDataPageHook.columnFilters)
  };
  console.log("form", form)
  const handleIndexSelect = (val: string) => {
    console.log(val)
    stockDataPageHook.setColumnFilters([{
      id: "stock_info.index",
      query: {
        "$in": [val]
      }
    }])
  }


  return (
    <Sheet>
      <SheetTrigger asChild>
        <Button className="mx-5" variant="outline">Screener</Button>
      </SheetTrigger>
      <SheetContent className="bg-white">
        <SheetHeader>
          <SheetTitle>Stocks Screener</SheetTitle>
        </SheetHeader>

        <Form {...form}>
          <form
            className="space-y-8, py-4"
          >
            <FormField
              control={form.control}
              name="stock_index"
              render={({ field }) => (
                <FormItem>
                  <Select
                    onValueChange={handleIndexSelect}
                    defaultValue={field.value}
                  >
                    <FormControl>
                      <SelectTrigger>
                        <SelectValue placeholder="Select a Index Group" />
                      </SelectTrigger>
                    </FormControl>
                    <SelectContent className="bg-white">
                      <SelectItem value="NIFTY50">Nifty 50</SelectItem>
                      <SelectItem value="NIFTY100">Nifty 100</SelectItem>
                      <SelectItem value="NIFTY200">Nifty 200</SelectItem>
                    </SelectContent>
                  </Select>
                  <div className="py-3">
                    <FormControl>
                      <RadioGroup
                        onValueChange={marketCapRadiohandle}
                        defaultValue={field.value}
                        className="flex flex-col space-y-1"
                      >
                        <FormItem className="flex items-center space-x-3 space-y-0">
                          <FormControl>
                            <RadioGroupItem value="large" />
                          </FormControl>
                          <FormLabel className="font-normal">
                            Large Cap
                          </FormLabel>
                        </FormItem>
                        <FormItem className="flex items-center space-x-3 space-y-0">
                          <FormControl>
                            <RadioGroupItem value="mid" />
                          </FormControl>
                          <FormLabel className="font-normal">Mid Cap</FormLabel>
                        </FormItem>
                        <FormItem className="flex items-center space-x-3 space-y-0">
                          <FormControl>
                            <RadioGroupItem value="small" />
                          </FormControl>
                          <FormLabel className="font-normal">
                            Small Cap
                          </FormLabel>
                        </FormItem>
                      </RadioGroup>
                    </FormControl>
                  </div>
                  <div>
                    {popOverFilters.map((filter) => {
                      // console.log(typeof filter)
                      if (filter == "volume") return <Input className="py-3" />
                      if (filter == "price") return <Slider />
                      if (filter == "debt") return <Input />
                      return null;
                    })}
                  </div>
                  <FormMessage />
                </FormItem>
              )}
            />
          </form>
        </Form>
        <SheetFooter>
          <div><CustomFilter setpopOverFilters={setpopOverFilters} popOverFilters={popOverFilters} /></div>
          <Button type="reset">Reset</Button>
        </SheetFooter>
      </SheetContent>
    </Sheet>
  );
}
