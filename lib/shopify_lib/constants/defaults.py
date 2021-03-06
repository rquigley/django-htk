HTK_SHOPIFY_SHOP_NAME = None
HTK_SHOPIFY_API_KEY = None
HTK_SHOPIFY_API_SECRET = None
HTK_SHOPIFY_SHARED_SECRET = None

HTK_SHOPIFY_MONGODB_COLLECTIONS = {
    # Products
    'product' : 'product',
    'product_tag' : 'product_tag',
    'product_image' : 'product_image',
    'product_variant' : 'product_variant',
    # Customers
    'customer' : 'customer',
    'customer_address' : 'customer_address',
    # Orders, Refunds, Fulfillments, Transactions
    'order' : 'order',
    'order_line_item' : 'order_line_item',
    'fulfillment' : 'fulfillment',
    'refund' : 'refund',
    'transaction' : 'transaction',
}

HTK_SHOPIFY_MONGODB_ITEM_PK = lambda item_type, item_json: item_json['id']

HTK_SHOPIFY_SQL_MODELS = {
    # Products
    'product' : 'shopify.ShopifyProduct',
    'product_tag' : 'shopify.ShopifyProductTag',
    'product_image' : 'shopify.ShopifyProductImage',
    'product_variant' : 'shopify.ShopifyProductVariant',
    # Customers
    'customer' : 'shopify.ShopifyCustomer',
    'customer_address' : 'shopify.ShopifyCustomerAddress',
    # Orders, Refunds, Fulfillments, Transactions
    'order' : 'shopify.ShopifyOrder',
    'order_line_item' : 'shopify.ShopifyOrderLineItem',
    'fulfillment' : 'shopify.ShopifyFulfillment',
    'refund' : 'shopify.ShopifyRefund',
    'transaction' : 'shopify.ShopifyTransaction',
}
