# file: simplefix_example.py
import simplefix

# Build a FIX message
builder = simplefix.FixMessage()
builder.append_pair(8, 'FIX.4.2')        # BeginString
builder.append_pair(35, 'D')             # MsgType = NewOrderSingle
builder.append_pair(49, 'SENDER')        # SenderCompID
builder.append_pair(56, 'TARGET')        # TargetCompID
builder.append_pair(11, 'ORDER-123')     # ClOrdID
builder.append_pair(54, '1')             # Side = Buy
builder.append_pair(55, 'AAPL')          # Symbol
builder.append_pair(60, simplefix.UtcTimestamp())  # TransactTime
builder.append_pair(40, '2')             # OrdType = Limit
builder.append_pair(44, '150.25')        # Price

raw = builder.encode()

print("Raw FIX message:", raw)

# Parse a FIX message
parser = simplefix.FixParser()
parser.append_buffer(raw)
msg = parser.get_message()   # returns a list-like structure
print("Parsed fields:", msg.body_dict)  # dict of tag->value
