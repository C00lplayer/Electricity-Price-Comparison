<a id="readme-top"></a>
<h1 align="center">Electricity Price Comparison</h1>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#type-of-output">Type of Output</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#index">Index</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

* Using data for available electricity plans
* I scraped electricity plan prices from this [website]
* Then using past usage data I calculated the cost of each plan for each past billing month
* Finally I graphed the cost of the 10 cheapest plans and the current plan over previous months

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [Matplotlib]
* [json]
* [request]
* [beautifulsoup4]
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

In this project I used the Powercor electricity network but this can be used with any electricity network, to change the electricity network see below:

### Prerequisites

To set the webscraper to your electricity network change the following:
* In line 22 of  Collecting Base Data.py add you state instead of 'vic' (in lowercase) and electricity network instead of 'powercor' (with a `#` at the start):
    * For example if I wanted to use the NSW - Ausgrid Network line 22 would look like this:
  ```python
  "https://wattever.com.au/compare-best-electricity-rates-nsw/#ausgrid"
  ```
* In line 40 of Collecting Base Data.py you need to change the table number (refer to the index below for the number):
    * Using the same example as above:
      ```python
      rows = soup.select('#table_1 tbody tr')
      ```
* In line 63 of Collecting Base Data.py you add your electricity network instead of 'powercor' inside the `' '`
   * Using the same example as above:
     ```python
     if 'Ausgrid' in h3_tag.text:
     ```
* Finally in line 71 of Collecting Base Data.py you need to change the anytime tariff code (refer to the index below for the number):
    * Using the same example as above:
      ```python
      if plan_info[4].text == 'EA010':
      ```

### Type of Output

* If you want to analyse only 1 specific month run the `Calculating Prices for specific month.py` file after making the following changes:
    * In line 88-89 enter your usage in KwH for that period and the number of days in that period, e.g:
    ```python
    SPECIFIC_MONTH_USAGE = 100
    DAYS_IN_THAT_PERIOD= 31 
    ```

* If you want to generate a graph comparing the 10 cheapest plans with your current plan run the `Analysis of Plans.py` file after marking the following changes:
    * You need to input your current plan details in lines 9-12 which are:
    * Your pay on time discount (if there is none put it as 1)
    * Your general usage charge
    * Your  supply charge
    * And finally your usage in KWH for each period
      ```python
      PAYONTIMEDISCOUNT = "Enter current pay on time discount here"
      Current_General = "Enter Current general usage charge here"
      Current_Supply =  "EnterCurrent supply charge here"
      Current_usage = {"Aug 2023": "Enter usage in KWH" , "Sep 2023": "Enter usage in KWH" ,"Oct 2023": "Enter usage in KWH" , "Nov 2023": "Enter usage in KWH", "Dec 2023": "Enter usage in KWH" ,"Jan 2024":"Enter usage in KWH", "Feb 2024": "Enter usage in KWH", "Mar 2024": "Enter usage in KWH", "Apr 2024": "Enter usage in KWH", "May 2024": "Enter usage in KWH"}
      ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

After running the program which graphs the plans you should end up with a graph with your current plan vs. the other top 10 cheapest plans as seen below:

![Screenshot comparision graph.](https://github.com/C00lplayer/Electricity-Price-Comparison/blob/main/Graph%20of%20Plans%20Over%20Time.png?raw=true)

Or if you run the program which analysis only 1 specific month you should end up with a csv file which contains all the plans sorted by the cheapest plan first like this: [CSV File]
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Index

| State/Territory and Electricity Network  | Table Number | Anytime Tariff Code|
| ------------- | ------------- | ------------- |
| NSW - Ausgrid  | #table_1  | EA010  |
| NSW - Endeavour  | #table_3  | N70  |
| NSW - Essential  | #table_6  | BLNN2AU  |
| QLD - EnergeX  | #table_1  | 8400  |
| VIC - AusNet  | #table_1  | NEE13  |
| VIC - CitiPower  | #table_3  | C1R  |
| VIC - Jemena  | #table_6  | A100  |
| VIC -PowerCor  | #table_8  | D1  |
| VIC - United  | #table_11  | LVS1R  |

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[website]: https://wattever.com.au/compare-best-electricity-rates-vic/#powercor
[Matplotlib]: https://matplotlib.org/
[json]: https://www.json.org
[request]: https://pypi.org/project/requests/
[beautifulsoup4]: https://pypi.org/project/beautifulsoup4/
[CSV File]: https://github.com/C00lplayer/Electricity-Price-Comparison/blob/main/sorted-plans-for-specific-month.csv

