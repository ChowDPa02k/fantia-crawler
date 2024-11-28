import argparse
import os
from .crawler import FantiaCrawler

def main():
    parser = argparse.ArgumentParser(description="Fantia Metadata Crawler")
    parser.add_argument('-e', '--email', 
                        default='', 
                        help='Fantia account email')
    parser.add_argument('-p', '--password', 
                        default='', 
                        help='Fantia account password')
    parser.add_argument('-d', '--directory', 
                        default=os.getcwd(), 
                        help='Directory to process videos (default: current directory)')
    
    args = parser.parse_args()
    
    try:
        crawler = FantiaCrawler(args.email, args.password)
        crawler.login()
        crawler.process_videos(args.directory)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        crawler.teardown()

if __name__ == '__main__':
    main()