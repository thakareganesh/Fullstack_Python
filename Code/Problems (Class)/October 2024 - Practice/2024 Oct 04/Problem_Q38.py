"""
Question 38: Mr. Venkat Reddy booked a flight ticket in Indian Airlines to travel Hyderabad to Vijayawada.
General ticket cost is 3450 and extra gst as 18%. but if he booked ticket in IndiGo ticket cost is 3200 and
extra gst as 12%. So how much amount he saved if he booked ticket in IndiGo.
"""

# Indian Airlines ticket costs
ia_general_tkt = 3450
ia_tkt_gst = 18
ia_tkt_gst_amt = ia_general_tkt * ia_tkt_gst / 100
print("Indian Airlines ticket GST cost:",ia_tkt_gst_amt)

ia_tkt_bill = ia_general_tkt + ia_tkt_gst_amt
print("Indian Airlines general ticket cost:",ia_tkt_bill)

# IndiGo tickets costs
ig_general_tkt = 3200
ig_tkt_gst = 12
ig_tkt_gst_amt = ig_general_tkt * ig_tkt_gst / 100
print("IndiGo ticket GST cost:",ig_tkt_gst_amt)

ig_tkt_bill = ig_general_tkt + ig_tkt_gst_amt
print("IndiGo general ticket cost:",ig_tkt_bill)

# calculating differance for saving
saving_money = ia_tkt_bill - ig_tkt_bill
print("Mr. Venkat Reddy saving amount if he books ticket in IndiGo:",saving_money)