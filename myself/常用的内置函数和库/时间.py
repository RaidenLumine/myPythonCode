import time

def get_current_time():
    """获取当前时间的时间戳和格式化字符串"""
    timestamp = time.time()
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
    return timestamp, formatted_time

def time_difference(start_time, end_time):
    """计算两个时间点之间的差异，返回秒数"""
    return end_time - start_time

def format_time(timestamp, format_string="%Y-%m-%d %H:%M:%S"):
    """将时间戳格式化为指定格式的字符串"""
    return time.strftime(format_string, time.localtime(timestamp))

def sleep_for_seconds(seconds):
    """暂停程序执行指定的秒数"""
    time.sleep(seconds)
    
def getTime():
    return time.time()

def getCtime():
    return time.ctime()
    
if __name__ == "__main__":
    # start_timestamp, start_formatted = get_current_time()
    # print(f"Start Time: {start_formatted} (Timestamp: {start_timestamp})")
    
    # print("Sleeping for 2 seconds...")
    # sleep_for_seconds(2)
    
    end_timestamp, end_formatted = get_current_time()
    # print(f"End Time: {end_formatted} (Timestamp: {end_timestamp})")
    
    # diff = time_difference(start_timestamp, end_timestamp)
    # print(f"Time Difference: {diff} seconds")
    
    custom_format = format_time(end_timestamp, "%A, %B %d, %Y %I:%M:%S %p")
    print(f"Formatted End Time: {custom_format}")
    
    # print(f"Current Timestamp: {getTime()}")
    
    # print(f"Current Ctime: {getCtime()}")