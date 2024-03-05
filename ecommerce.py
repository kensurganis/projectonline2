# dashboard.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    customers_df = pd.read_csv('customers_dataset.csv')
    geolocation_df = pd.read_csv('geolocation_dataset.csv')
    order_items_df = pd.read_csv('order_items_dataset.csv')
    order_payments_df = pd.read_csv('order_payments_dataset.csv')
    order_reviewers_df = pd.read_csv('order_reviewers_dataset.csv')
    orders_df = pd.read_csv('orders_dataset.csv')
    product_category_name_translation_df = pd.read_csv('product_category_name_translation.csv')
    products_df = pd.read_csv('products_dataset.csv')
    sellers_df = pd.read_csv('sellers_dataset.csv')

    dfs = [customers_df, geolocation_df, order_items_df, order_payments_df, order_reviewers_df, orders_df,
           product_category_name_translation_df, products_df, sellers_df]
    df = pd.concat(dfs, axis=0, ignore_index=True, sort=False)

    df = df.drop_duplicates()
    df = df.reset_index(drop=True)

    df = df.dropna()

    return df

def display_distribution_plot():
    sns.countplot(x='payment_type', hue='order_status', data=df)
    plt.title('Distribusi Jenis Pembayaran pada Setiap Status Pesanan')
    plt.xlabel('Jenis Pembayaran')
    plt.ylabel('Jumlah Pesanan')
    plt.legend()
    st.pyplot()

def display_box_plot():
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='product_category_name', y='price', data=df)
    plt.title('Distribusi Harga Produk pada Setiap Kategori')
    plt.xlabel('Kategori Produk')
    plt.ylabel('Harga')
    plt.xticks(rotation=45, ha='right')
    st.pyplot()

if __name__ == '__main__':
    st.title('E-Commerce Dashboard')

    df = load_data()

    st.subheader('Informasi Dasar dan Nilai Null')
    st.write(df.info())
    st.write(df.isnull().sum())

    st.subheader('Visualisasi Data')
    display_distribution_plot()
    display_box_plot()
