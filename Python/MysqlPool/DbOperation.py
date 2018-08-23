from Configuration.DBConnection import connection_pool_obj


# Whenever pool connection is closed it does't destroy it just return back to pool and will be available
# When new connection is requested 