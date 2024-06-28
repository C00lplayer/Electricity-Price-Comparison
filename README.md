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
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
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

To set the websraper to your electricity network change the following:
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
* Then you need to input your current plan details on lines 9-12 on Analysis of Plans.py
    * You need to enter your pay on time discount (if there is none put it as 1)
    * You need to enter your general usage charge
    * You need to enter your supply charge
    * And finally you need to enter you usage in KWH for each period
      ```python
      PAYONTIMEDISCOUNT = "Enter current pay on time discount here"
      Current_General = "Enter Current general usage charge here"
      Current_Supply =  "EnterCurrent supply charge here"
      Current_usage = {"Aug 2023": "Enter usage in KWH" , "Sep 2023": "Enter usage in KWH" ,"Oct 2023": "Enter usage in KWH" , "Nov 2023": "Enter usage in KWH", "Dec 2023": "Enter usage in KWH" ,"Jan 2024":"Enter usage in KWH", "Feb 2024": "Enter usage in KWH", "Mar 2024": "Enter usage in KWH", "Apr 2024": "Enter usage in KWH", "May 2024": "Enter usage in KWH"}
      ```

<!-- USAGE EXAMPLES -->
## Usage

After the program is run you should end up with a graph with your current plan vs. the other top 10 cheapest plans as seen below:

![Screenshot comparision graph.](https://github.com/C00lplayer/Electricity-Price-Comparison/blob/main/Graph%20of%20Plans%20Over%20Time.png?raw=true)

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


[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
