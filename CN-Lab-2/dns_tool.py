import dns.resolver

# --- Configuration ---
DOMAIN_TO_QUERY = 'google.com'
LOG_FILE = 'dns_log.txt'
RECORD_TYPES = ['A', 'MX', 'CNAME']

def query_dns(domain, log_file):
    """Performs DNS queries for various record types and logs the results."""
    print(f"--- Starting DNS queries for '{domain}' ---")
    print(f"Results will be logged to '{log_file}'")

    with open(log_file, 'w') as f:
        f.write(f"DNS Query Results for: {domain}\n")
        f.write("="*40 + "\n")

        for record_type in RECORD_TYPES:
            try:
                print(f"Querying for {record_type} records...")
                f.write(f"\n--- {record_type} Records ---\n")

                # Resolve the DNS record
                answers = dns.resolver.resolve(domain, record_type)
                
                for rdata in answers:
                    log_entry = f"{rdata.to_text()}\n"
                    print(f"  Found: {log_entry.strip()}")
                    f.write(log_entry)

            except dns.resolver.NoAnswer:
                log_entry = f"No {record_type} records found for {domain}.\n"
                print(f"  {log_entry.strip()}")
                f.write(log_entry)
            except dns.resolver.NXDOMAIN:
                log_entry = f"The domain '{domain}' does not exist.\n"
                print(f"  {log_entry.strip()}")
                f.write(log_entry)
                break # No need to query other records if domain doesn't exist
            except Exception as e:
                log_entry = f"An error occurred: {e}\n"
                print(f"  {log_entry.strip()}")
                f.write(log_entry)
    
    print(f"\n✅ All queries complete. Check '{log_file}' for details.")

if __name__ == "__main__":
    query_dns(DOMAIN_TO_QUERY, LOG_FILE)
    # You can uncomment the line below to test a CNAME lookup
    # query_dns('mail.google.com', 'dns_log_cname.txt')
