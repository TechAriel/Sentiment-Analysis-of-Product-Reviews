# Sentiment Analysis of Product Reviews

## Description
This project utilizes Natural Language Processing (NLP) techniques to analyze the sentiment of product reviews. By leveraging the capabilities of libraries like spaCy and TextBlob, it preprocesses the text data to remove noise and then assesses whether the sentiments expressed in reviews are positive, negative, or neutral. This analysis can provide invaluable insights for businesses looking to understand customer sentiment towards their products, helping them identify areas of improvement and enhance customer satisfaction.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Installation

To run this project locally, you need to have Python installed on your machine. Then, follow these steps:

1. Clone the repository to your local machine:
    ```
    git clone https://github.com/yourusername/yourprojectrepository.git
    ```
2. Navigate to the project directory:
    ```
    cd yourprojectdirectory
    ```
3. Install the required dependencies:
    ```
    pip install spacy textblob pandas
    ```
4. Download the necessary spaCy language model and TextBlob corpora:
    ```
    python -m textblob.download_corpora
    python -m spacy download en_core_web_sm
    ```

## Usage

After installing the project, you can run the sentiment analysis script as follows:

1. Ensure you have a dataset of product reviews in CSV format, with at least one column named 'reviews.text' containing the review texts.
2. Modify the script to point to your dataset file path:
    ```python
    file_path = '/path/to/your/amazon_product_reviews.csv'
    ```
3. Run the script:
    ```
    python sentiment_analysis.py
    ```
4. The script will preprocess the reviews, perform sentiment analysis, and print out the sentiment results for the first few reviews. Additionally, it will compare the similarity between two selected reviews.

### Screenshots



## Credits
This project was developed by [Gabriel Oduor](https://github.com/TechAriel). Special thanks to the spaCy and TextBlob libraries for providing the NLP tools necessary to complete this analysis.
