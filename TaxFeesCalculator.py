import tkinter as tk
from tkinter import ttk, messagebox

def calculate_final_price():
    try:
        item_prices = text_items.get("1.0", tk.END).strip().replace(",", "\n").split()
        item_prices = [float(price) for price in item_prices]
        itemp = sum(item_prices)
        aoi = len(item_prices)

        buyer_premium = 0.15
        lot_fee = 3 * aoi
        sales_tax = 0.07

        buyer_premium_fee = itemp * buyer_premium
        nfp = buyer_premium_fee + lot_fee + itemp
        tax_price = nfp * sales_tax
        final_price = nfp + tax_price

        result_macbid.set(f"The final price on MacBid is: ${final_price:.2f}")

        ebay_item_prices = text_ebay_items.get("1.0", tk.END).strip().replace(",", "\n").split()
        ebay_item_prices = [float(price) for price in ebay_item_prices]
        ebay_fees = sum(price * 0.15 for price in ebay_item_prices)

        ebay_prices_total = sum(ebay_item_prices)
        ebay_final_price = ebay_prices_total - ebay_fees
        finalfinalprice = ebay_final_price - final_price

        result_ebay.set(f"The final profit is: ${finalfinalprice:.2f}")
        if final_price != 0:
            profit_margin = (finalfinalprice / final_price) * 100
            result_profit.set(f"Your profit margin on this sale is {profit_margin:.2f}%")
        else:
            result_profit.set("Error: Final price is zero, cannot calculate profit margin.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

app = tk.Tk()
app.title("Price Calculator")
app.configure(bg="#000000")  # Set background color to black

# Style
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 14), background="#000000", foreground="#ffffff")  # Set text color to white
style.configure("TButton", font=("Helvetica", 14), background="#4CAF50", foreground="#ffffff")
style.configure("TFrame", background="#000000")

frame_main = ttk.Frame(app, padding="20", style="TFrame")
frame_main.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Colors for Text Widgets
text_bg_color = "#000000"
text_fg_color = "#ffffff"

# MacBid Items
ttk.Label(frame_main, text="Enter MacBid item prices (comma or newline separated):", foreground="#ffffff").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
text_items = tk.Text(frame_main, height=10, width=60, bg=text_bg_color, fg=text_fg_color, font=("Helvetica", 14))
text_items.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=(tk.W, tk.E))

# eBay Items
ttk.Label(frame_main, text="Enter eBay item prices (comma or newline separated):", foreground="#ffffff").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
text_ebay_items = tk.Text(frame_main, height=10, width=60, bg=text_bg_color, fg=text_fg_color, font=("Helvetica", 14))
text_ebay_items.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky=(tk.W, tk.E))

# Calculation and Results
ttk.Button(frame_main, text="Calculate Final Price", command=calculate_final_price).grid(row=4, column=0, columnspan=2, padx=10, pady=20, sticky=(tk.W, tk.E))

result_macbid = tk.StringVar()
ttk.Label(frame_main, textvariable=result_macbid, font=("Helvetica", 14, "bold"), foreground="#ffffff").grid(row=5, column=0, columnspan=2, padx=10, pady=10)

result_ebay = tk.StringVar()
ttk.Label(frame_main, textvariable=result_ebay, font=("Helvetica", 14, "bold"), foreground="#ffffff").grid(row=6, column=0, columnspan=2, padx=10, pady=10)

result_profit = tk.StringVar()
ttk.Label(frame_main, textvariable=result_profit, font=("Helvetica", 14, "bold"), foreground="#ffffff").grid(row=7, column=0, columnspan=2, padx=10, pady=10)

app.mainloop()