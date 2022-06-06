def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)

    total_emails_sent_by_sender = {}

    for line in handle:
        if line.startswith('From'):
            if line.startswith('From:'):
                continue
            else:
                sections_of_line = line.split(' ')
                senders_email_address = sections_of_line[1]
                if senders_email_address in total_emails_sent_by_sender:
                    total_emails_sent_by_sender[senders_email_address] += 1
                else:
                    total_emails_sent_by_sender[senders_email_address] = 1
    
    max_emails_sent = 0
    senders_email = ''

    for key in total_emails_sent_by_sender:
        if total_emails_sent_by_sender[key] > max_emails_sent:
            max_emails_sent = total_emails_sent_by_sender[key]
            senders_email = key
    
    print(senders_email, max_emails_sent)
        
        
## if you want to test locally before you try to sync
## uncomment countEmail() and run > python counter.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
countEmail()
