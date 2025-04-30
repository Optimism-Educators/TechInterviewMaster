# InterView Question

### **1. Project Overview & Business Context**

- What was the goal of this project, and how did it align with business objectives?
- How did you define "underperforming regions"? What metrics did you use?
- Why did you choose ARIMA/SARIMA instead of simpler models like linear regression or machine learning models?
- How did you ensure your recommendations (to boost revenue by 12%) were actionable for stakeholders?

---

### **2. Data Collection & Preprocessing**

- Where did you source the sales data from (e.g., internal databases, APIs)?  
- How did you handle missing values or outliers in the historical sales data?  
- Did you aggregate the data at a daily/monthly/yearly level? Why?  
- How did you validate the quality of the data before analysis?  
- Did you engineer any features (e.g., lag variables, rolling averages) for the time-series model?  

---

### **3. Statistical Analysis & Modeling**

- What steps did you take to check for stationarity in the time series?  
- How did you determine the order of differencing (d) in the ARIMA model?  
- Why did you choose SARIMA over ARIMA? What seasonal patterns did you observe?  
- How did you evaluate the model’s performance (e.g., MAE, RMSE, MAPE)?  
- Did you perform cross-validation for time-series forecasting? If yes, how?  
- How did you interpret the ACF/PACF plots for model selection?  
- What hyperparameters did you tune for the model?  

---

### **4. Visualization & Reporting**

- How did you visualize trends and seasonality in Tableau/Power BI?  
- Did you create dashboards for stakeholders? What key metrics were included (e.g., YoY growth, region-wise comparisons)?  
- How did you explain complex statistical concepts (e.g., stationarity, seasonality) to non-technical audiences?  
- What tools did you use to present the forecasted sales visually?  

---

### **5. Business Impact & Recommendations**

- How did your analysis lead to actionable recommendations for underperforming regions?  
- How did you quantify the potential revenue uplift of 12%?  
- Did you collaborate with sales/marketing teams to implement your suggestions?  
- How did you prioritize which regions to target first?  

---

### **6. Challenges & Problem-Solving**

- What were the biggest challenges during this project (e.g., data quality, model accuracy)?  
- How did you handle external factors (e.g., market trends, holidays) affecting sales forecasts?  
- If the model’s predictions were inaccurate, what steps would you take to improve it?  

---

### **7. Technical Depth (Python/SQL/Statsmodels)**

- Can you walk us through the Python code for fitting the SARIMA model?  
- How did you split the data into training and testing sets?  
- Share an example of a SQL query you wrote to extract historical sales data.  
- How did you decompose the time series into trend, seasonality, and residuals?  

---

### **8. Hypothetical Scenarios**

- If the sales data had multiple seasonal cycles (e.g., weekly and yearly), how would you adjust your model?  
- How would you handle missing data in a critical region where forecasts are needed?  
- Suppose new sales data comes in mid-forecast period—how would you update the model?  

---

### **9. Communication & Stakeholder Management**

- How did you present your findings to executives versus operational teams?  
- What feedback did stakeholders give on your recommendations?  
- How did you ensure alignment between your analytical approach and business goals?  

---

### **10. Advanced Concepts**

- Have you compared ARIMA/SARIMA with alternative models like Prophet or LSTM?  
- How did you account for uncertainty in forecasts (e.g., confidence intervals)?  
- What steps would you take to automate this forecasting pipeline?  

---

### **How to Prepare: Pro Tips**

1. **Practice Explaining Technical Terms Simply**:  
   - Example: *"SARIMA helps predict sales by capturing repeating patterns (like holiday spikes) in the data."*  

2. **Bring Code Snippets**:  
   - Be ready to share Python code for SARIMA, data cleaning, or visualization.  

3. **Quantify Everything**:  
   - Use metrics like "RMSE of 50 units" or "12% revenue increase" to back your claims.  

4. **Prepare Visual Examples**:  
   - Show screenshots of your Tableau dashboard (if allowed).  

5. **Anticipate Follow-Ups**:  
   - If you mention handling seasonality, be ready to explain Fourier transforms or dummy variables for cyclic patterns.