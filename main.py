import requests
import json

# Define the list of flowers
flowers = ["rose", "tulip", "sunflower", "lily", "orchid"]

# Define the server's API endpoint for generating images
api_endpoint = "https://example.com/api/generate_flower_image"

# Define a function to fetch images for a given flower
def fetch_flower_image(flower_name):
    try:
        # Prepare the payload for the API request
        payload = {"flower": flower_name}
        
        # Make the API request
        response = requests.post(api_endpoint, json=payload)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Assuming the response contains an 'image_url' field
            image_url = data.get("image_url")
            if image_url:
                return image_url
            else:
                print(f"No image URL found for flower: {flower_name}")
                return None
        else:
            print(f"Failed to fetch image for flower: {flower_name}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred while fetching image for flower: {flower_name}. Error: {e}")
        return None

# Main function to fetch and display images for all flowers
def main():
    for flower in flowers:
        print(f"Fetching image for: {flower}")
        image_url = fetch_flower_image(flower)
        if image_url:
            print(f"Image URL for {flower}: {image_url}")
        else:
            print(f"Could not retrieve image for {flower}")

if __name__ == "__main__":
    main()
