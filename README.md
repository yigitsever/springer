# springer
Python script to download Springer Books released for free during the 2020 COVID-19 quarantine

# Download excel file from:
https://www.springernature.com/gp/librarians/news-events/all-news-articles/industry-news-initiatives/free-access-to-textbooks-for-institutions-affected-by-coronaviru/17855960

or

```bash
curl https://resource-cms.springernature.com/springer-cms/rest/v1/content/17858272/data/v5 -o books.xlsx
```

You can filter and copy download links saved as `links.txt`
If you saved another name file you should change `links.txt` file name in line 13
The python script and `links.txt` files must be under the same directory

Not: the script requires python3 because of `urllib.request` module

## A Slightly Curated List

- A Beginners Guide to Python 3 Programming               - https://link.springer.com/book/10.1007%2F978-3-030-20290-3
- A Beginner’s Guide to R                                 - https://link.springer.com/book/10.1007%2F978-0-387-93837-0
- Advanced Guide to Python 3 Programming                  - https://link.springer.com/book/10.1007%2F978-3-030-25943-3
- All of Statistics                                       - https://link.springer.com/book/10.1007%2F978-0-387-21736-9
- A Modern Introduction to Probability and Statistics     - https://link.springer.com/book/10.1007%2F1-84628-168-7
- Analysis for Computer Scientists                        - https://link.springer.com/book/10.1007%2F978-3-319-91155-7
- An Introduction to Machine Learning                     - https://link.springer.com/book/10.1007%2F978-3-319-63913-0
- A Primer on Scientific Programming with Python          - https://link.springer.com/book/10.1007%2F978-3-662-49887-3
- Automata and Computability                              - https://link.springer.com/book/10.1007%2F978-1-4612-1844-9
- Bayesian and Frequentist Regression Methods             - https://link.springer.com/book/10.1007%2F978-1-4419-0925-1
- Concise Guide to Software Engineering                   - https://link.springer.com/book/10.1007%2F978-3-319-57750-0
- Cryptography Made Simple                                - https://link.springer.com/book/10.1007%2F978-3-319-21936-3
- Data Structures and Algorithms with Python              - https://link.springer.com/book/10.1007%2F978-3-319-13072-9
- Differential Equations and Their Applications           - https://link.springer.com/book/10.1007%2F978-1-4612-4360-1
- Discrete Mathematics                                    - https://link.springer.com/book/10.1007%2Fb97469
- Foundations of Programming Languages                    - https://link.springer.com/book/10.1007%2F978-3-319-70790-7
- Global Supply Chain and Operations Management           - https://link.springer.com/book/10.1007%2F978-3-319-94313-8
- Guide to Competitive Programming                        - https://link.springer.com/book/10.1007%2F978-3-319-72547-5
- Guide to Computer Network Security                      - https://link.springer.com/book/10.1007%2F978-3-319-55606-2
- Guide to Discrete Mathematics                           - https://link.springer.com/book/10.1007%2F978-3-319-44561-8
- Internet of Things From Hype to Reality                 - https://link.springer.com/book/10.1007%2F978-3-319-99516-8
- Introduction to Artificial Intelligence                 - https://link.springer.com/book/10.1007%2F978-3-319-58487-4
- Introduction to Data Science                            - https://link.springer.com/book/10.1007%2F978-3-319-50017-1
- Introduction to Deep Learning                           - https://link.springer.com/book/10.1007%2F978-3-319-73004-2
- Introduction to Electronic Commerce and Social Commerce - https://link.springer.com/book/10.1007%2F978-3-319-50091-1
- Introduction to Evolutionary Computing                  - https://link.springer.com/book/10.1007%2F978-3-662-44874-8
- Introduction to Parallel Computing                      - https://link.springer.com/book/10.1007%2F978-3-319-98833-7
- Introduction to Partial Differential Equations          - https://link.springer.com/book/10.1007%2F978-3-319-48936-0
- LaTeX in 24 Hours                                       - https://link.springer.com/book/10.1007%2F978-3-319-47831-9
- Linear Algebra Done Right                               - https://link.springer.com/book/10.1007%2F978-3-319-11080-6
- Linear Algebra                                          - https://link.springer.com/book/10.1007%2F978-3-319-24346-7
- Linear and Nonlinear Programming                        - https://link.springer.com/book/10.1007%2F978-3-319-18842-3
- Linear Programming                                      - https://link.springer.com/book/10.1007%2F978-1-4614-7630-6
- Methods of Mathematical Modelling                       - https://link.springer.com/book/10.1007%2F978-3-319-23042-9
- Multimedia Big Data Computing for IoT Applications      - https://link.springer.com/book/10.1007%2F978-981-13-8759-3
- Neural Networks and Deep Learning                       - https://link.springer.com/book/10.1007%2F978-3-319-94463-0
- Of Cigarettes, High Heels, and Other Interesting Things - https://link.springer.com/book/10.1057%2F978-1-349-95348-6
- Philosophy of Science for Scientists                    - https://link.springer.com/book/10.1007%2F978-3-319-26551-3
- Probability and Statistics for Computer Science         - https://link.springer.com/book/10.1007%2F978-3-319-64410-3
- Probability                                             - https://link.springer.com/book/10.1007%2F978-1-4612-4374-8
- Probability Theory                                      - https://link.springer.com/book/10.1007%2F978-1-4471-5201-9
- Python Programming Fundamentals                         - https://link.springer.com/book/10.1007%2F978-1-4471-6642-9
- Reading, Writing, and Proving                           - https://link.springer.com/book/10.1007%2F978-1-4419-9479-0
- Supply Chain Management and Advanced Planning           - https://link.springer.com/book/10.1007%2F978-3-642-55309-7
- Sustainable Supply Chains                               - https://link.springer.com/book/10.1007%2F978-3-319-29791-0
- Systems Programming in Unix/Linux                       - https://link.springer.com/book/10.1007%2F978-3-319-92429-8
- The Algorithm Design Manual                             - https://link.springer.com/book/10.1007%2F978-1-84800-070-4
- The Joy of Science                                      - https://link.springer.com/book/10.1007%2F978-1-4020-6099-1
- The Nature of Scientific Knowledge                      - https://link.springer.com/book/10.1007%2F978-3-319-33405-9
- The Python Workbook                                     - https://link.springer.com/book/10.1007%2F978-3-319-14240-1
- Time Series Analysis                                    - https://link.springer.com/book/10.1007%2F978-0-387-75959-3
- Understanding Cryptography                              - https://link.springer.com/book/10.1007%2F978-3-642-04101-3
- Writing for Publication                                 - https://link.springer.com/book/10.1007%2F978-3-319-31650-5
