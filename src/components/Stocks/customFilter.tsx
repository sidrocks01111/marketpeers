import { Button } from "@/components/ui/button";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";
import { useForm } from "react-hook-form";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";

import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";

import { Checkbox } from "@/components/ui/checkbox";
import { Dispatch, SetStateAction } from "react";

const customFilterItems = [
  {
    id: "volume",
    label: "Volume",
  },
  {
    id: "price",
    label: "Price",
  },
  {
    id: "debt",
    label: "debt",
  },
] as const;

const FormSchema = z.object({
  items: z.array(z.string()).refine((value) => value.some((item) => item), {
    message: "You have to select at least one item.",
  }),
});

interface customeFilterProps {
  setpopOverFilters: Dispatch<SetStateAction<string[]>>
  popOverFilters: string[]
}

export function CustomFilter({ setpopOverFilters, popOverFilters }: customeFilterProps) {
  const form = useForm<z.infer<typeof FormSchema>>({
    resolver: zodResolver(FormSchema),
    defaultValues: {
      items: [],
    },
  });

  function onSubmit(data: z.infer<typeof FormSchema>) {
    console.log(data);
    setpopOverFilters(data["items"])
  }

  return (
    <Popover>
      <PopoverTrigger asChild>
        <Button variant="outline">Add Filter</Button>
      </PopoverTrigger>
      <PopoverContent className="w-80">
        <div className="grid gap-4">
          <div className="space-y-2">
            <h4 className="font-medium leading-none">Select Filters</h4>
            <Form {...form}>
              <form
                onSubmit={form.handleSubmit(onSubmit)}
                className="space-y-8"
              >
                <FormField
                  control={form.control}
                  name="items"
                  render={() => (
                    <FormItem>
                      <div className="mb-4">
                        {/* <FormLabel className="text-base">Sidebar</FormLabel> */}
                        <FormDescription>
                          Select the filter to add
                        </FormDescription>
                      </div>
                      {customFilterItems.map((item) => (
                        <FormField
                          key={item.id}
                          control={form.control}
                          name="items"
                          render={({ field }) => {
                            return (
                              <FormItem
                                key={item.id}
                                className="flex flex-row items-start space-x-3 space-y-0"
                              >
                                <FormControl>
                                  <Checkbox
                                    checked={field.value?.includes(item.id)}
                                    onCheckedChange={(checked) => {
                                      return checked
                                        ? field.onChange([
                                            ...field.value,
                                            item.id,
                                          ])
                                        : field.onChange(
                                            field.value?.filter(
                                              (value) => value !== item.id
                                            )
                                          );
                                    }}
                                  />
                                </FormControl>
                                <FormLabel className="text-sm font-normal">
                                  {item.label}
                                </FormLabel>
                              </FormItem>
                            );
                          }}
                        />
                      ))}
                      <FormMessage />
                    </FormItem>
                  )}
                />
                <Button type="submit">Submit</Button>
              </form>
            </Form>
          </div>
        </div>
      </PopoverContent>
    </Popover>
  );
}
