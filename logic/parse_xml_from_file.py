import os
import xml.etree.ElementTree as ET

def parse_xml_from_file(filename):
    # Check if file exists
    if not os.path.isfile(filename):
        raise ValueError(f"{filename} does not exist.")

    with open(filename, "r") as f:
        # Read the line from the file
        line = f.readline().strip()

    # Split the line into ref_no and xml data
    ref_no, xml_data = line.split("#####")

    # Parse the xml data using ElementTree
    root = ET.fromstring(xml_data)

    # # Extract and return relevant information
    # transaction_id = root.find(".//BizMsgIdr").text
    # sender_bic = root.find(".//Fr/FIId/FinInstnId/BICFI").text
    # receiver_bic = root.find(".//To/FIId/FinInstnId/BICFI").text
    # amount = root.find(".//IntrBkSttlmAmt").text
    # currency = root.find(".//IntrBkSttlmAmt").attrib["Ccy"]
    #
    # return {
    #     "ref_no": ref_no,
    #     "transaction_id": transaction_id,
    #     "sender_bic": sender_bic,
    #     "receiver_bic": receiver_bic,
    #     "amount": amount,
    #     "currency": currency
    # }
    # extract payment information
    payment_info = {}
    payment_info['instruction_id'] = root.find('.///PmtId/InstrId').text
    payment_info['end_to_end_id'] = root.find('.//PmtId/EndToEndId').text
    payment_info['uetr'] = root.find('.//PmtId/UETR').text
    payment_info['amount'] = float(root.find('.//IntrBkSttlmAmt').text)
    payment_info['currency'] = root.find('.//IntrBkSttlmAmt').get('Ccy')
    payment_info['value_date'] = root.find('.//IntrBkSttlmDt').text

    # extract debitor information
    debitor_info = {}
    debitor_info['name'] = root.find('.//Dbtr/Nm').text
    debitor_info['address'] = ', '.join(root.findall('.//Dbtr/PstlAdr/Adrline').text)
    debitor_info['account_id'] = root.find('.//DbtrAcct/Id/Othr/Id').text

    # extract creditor information
    creditor_info = {}
    creditor_info['name'] = root.find('.//Cdtr/Nm').text
    creditor_info['address'] = ', '.join(root.findall('.//Cdtr/PstlAdr/AdrLine').text)
    creditor_info['account_id'] = root.find('.//CdtrAcct/Id/Othr/Id').text

    return ref_no, payment_info, debitor_info, creditor_info

file_name ="/Users/arun/PycharmProjects/xml/data/brains/BRAINS.MX.TXT"
result = parse_xml_from_file(file_name)
print(result)