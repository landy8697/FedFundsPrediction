This project implements different types of models to predict future federal funds rate, which is a measure that highly impacts the cost of borrowing money as well as stock market movements.

**Taylor Rule**

The Taylor Rule is an equation linking the Federal Reserve's benchmark interest rate to levels of inflation and economic growth. Created by Economist John Taylor, the model assumes Taylor recommends the real interest rate should be 1.5 times the inflation rate and the equilibrium federal funds rate of 2% above inflation.

Monthly Version:
rt =  2  +  pt - 1 + 1/2 (pt - 1 – 2) + 1/2(ut – 1 – 4)         

Where:
rt = fed funds rate at t  
pt - 1 = lagged monthly inflation measured by CPI 
ut – 1 = lagged monthly unemployment rate 

**Econometric Model**

