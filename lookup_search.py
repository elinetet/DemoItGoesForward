# Imports
import pandas as pd


class Lookup:
    @staticmethod
    def demo_lookup(fixed, window_sell, window_del, prod):
        if prod == 'A':
            SKU = 114230005
        elif prod == 'B':
            SKU = 116410045
        elif prod == 'C':
            SKU = 114810003
        elif prod == 'D':
            SKU = 141020116
        elif prod == 'E':
            SKU = 113122398

        lookup = pd.read_pickle('lookuptable_demo2.pkl')

        lookID = str(int(fixed))+','+str(window_sell)+','+str(window_del)
        results = lookup[SKU][lookID]
        return results

    @staticmethod
    def demo_lookupco2(inleg, window_sell, window_del, prod):
        if prod == 'A':
            SKU = 114230005
        elif prod == 'B':
            SKU = 116410045
        elif prod == 'C':
            SKU = 114810003
        elif prod == 'D':
            SKU = 141020116
        elif prod == 'E':
            SKU = 113122398

        lookup = pd.read_pickle('lookuptable_co2_2.pkl')

        lookID = str(window_sell)+','+str(window_del)+','+str(inleg)
        results = lookup[SKU][lookID]
        return results


    @staticmethod
    def demo_lookupco2_discount(inleg, prod):
        if prod == 'A':
            SKU = 114230005
        elif prod == 'B':
            SKU = 116410045
        elif prod == 'C':
            SKU = 114810003
        elif prod == 'D':
            SKU = 141020116
        elif prod == 'E':
            SKU = 113122398

        lookup = pd.read_pickle('lookuptable_co2_2.pkl')

        lookID = str(2)+','+str(2)+','+str(inleg)
        results = lookup[SKU][lookID]
        discount = results[6]
        return discount
