Perfect. Now we move from “AI agents” → decision intelligence system.

I’ll structure this into 4 production-ready components:

🧠 Numerical Scoring Formula

📊 Composite Recommendation Score

🚀 Startup-Ready Architecture Diagram

🔎 RAG Retrieval Structure Per Dataset

🧠 1. Numerical Scoring Formula

We convert each analytical dimension into a normalized score (0–100).

1️⃣ Financial Sustainability Score (FSS) – 0–100

From: carpurchase.csv

Core Ratios

A. Debt-to-Income (DTI)

𝐷
𝑇
𝐼
=
𝐶
𝑟
𝑒
𝑑
𝑖
𝑡
𝐶
𝑎
𝑟
𝑑
𝐷
𝑒
𝑏
𝑡
𝐴
𝑛
𝑛
𝑢
𝑎
𝑙
𝑆
𝑎
𝑙
𝑎
𝑟
𝑦
DTI=
AnnualSalary
CreditCardDebt
	​


Score mapping:

DTI	Score
< 0.15	100
0.15–0.30	75
0.30–0.50	50
> 0.50	25

B. Income-to-Car-Price Ratio (ICR)

𝐼
𝐶
𝑅
=
𝐴
𝑛
𝑛
𝑢
𝑎
𝑙
𝑆
𝑎
𝑙
𝑎
𝑟
𝑦
𝐶
𝑎
𝑟
𝑃
𝑟
𝑖
𝑐
𝑒
ICR=
CarPrice
AnnualSalary
	​

ICR	Score
≥ 1.0	100
0.7–1.0	75
0.5–0.7	50
< 0.5	25

C. Net Worth Buffer (NWB)

𝑁
𝑊
𝐵
=
𝑁
𝑒
𝑡
𝑊
𝑜
𝑟
𝑡
ℎ
𝐶
𝑎
𝑟
𝑃
𝑟
𝑖
𝑐
𝑒
NWB=
CarPrice
NetWorth
	​

NWB	Score
≥ 2	100
1–2	75
0.5–1	50
< 0.5	25
Final Financial Sustainability Score:
𝐹
𝑆
𝑆
=
0.4
(
𝐷
𝑇
𝐼
_
𝑆
𝑐
𝑜
𝑟
𝑒
)
+
0.3
(
𝐼
𝐶
𝑅
_
𝑆
𝑐
𝑜
𝑟
𝑒
)
+
0.3
(
𝑁
𝑊
𝐵
_
𝑆
𝑐
𝑜
𝑟
𝑒
)
FSS=0.4(DTI_Score)+0.3(ICR_Score)+0.3(NWB_Score)
2️⃣ Loan Feasibility Score (LFS) – 0–100

From: loanapproval.csv

Credit Score Mapping
Credit Score	Score
750+	100
700–749	80
650–699	60
600–649	40
<600	20
Asset Strength Ratio
𝐴
𝑠
𝑠
𝑒
𝑡
𝑅
𝑎
𝑡
𝑖
𝑜
=
𝐵
𝑎
𝑛
𝑘
𝐴
𝑠
𝑠
𝑒
𝑡
𝑠
+
𝑅
𝑒
𝑠
𝑖
𝑑
𝑒
𝑛
𝑡
𝑖
𝑎
𝑙
𝐴
𝑠
𝑠
𝑒
𝑡
𝑠
𝐿
𝑜
𝑎
𝑛
𝐴
𝑚
𝑜
𝑢
𝑛
𝑡
AssetRatio=
LoanAmount
BankAssets+ResidentialAssets
	​


Mapped to 25–100 scale.

𝐿
𝐹
𝑆
=
0.6
(
𝐶
𝑟
𝑒
𝑑
𝑖
𝑡
𝑆
𝑐
𝑜
𝑟
𝑒
𝑆
𝑐
𝑜
𝑟
𝑒
)
+
0.4
(
𝐴
𝑠
𝑠
𝑒
𝑡
𝑅
𝑎
𝑡
𝑖
𝑜
𝑆
𝑐
𝑜
𝑟
𝑒
)
LFS=0.6(CreditScoreScore)+0.4(AssetRatioScore)
3️⃣ Market Value Efficiency Score (MVES) – 0–100

From: usedcars.csv

𝑉
𝑎
𝑙
𝑢
𝑒
𝐼
𝑛
𝑑
𝑒
𝑥
=
𝑀
𝑜
𝑑
𝑒
𝑙
𝑌
𝑒
𝑎
𝑟
𝑃
𝑟
𝑖
𝑐
𝑒
ValueIndex=
Price
ModelYear
	​

𝑀
𝑖
𝑙
𝑒
𝑎
𝑔
𝑒
𝐸
𝑓
𝑓
𝑖
𝑐
𝑖
𝑒
𝑛
𝑐
𝑦
=
1
𝑀
𝑖
𝑙
𝑒
𝑎
𝑔
𝑒
/
1000
MileageEfficiency=
Mileage/1000
1
	​


Normalize both 0–100:

𝑀
𝑉
𝐸
𝑆
=
0.6
(
𝑉
𝑎
𝑙
𝑢
𝑒
𝐼
𝑛
𝑑
𝑒
𝑥
𝑆
𝑐
𝑜
𝑟
𝑒
)
+
0.4
(
𝑀
𝑖
𝑙
𝑒
𝑎
𝑔
𝑒
𝐸
𝑓
𝑓
𝑖
𝑐
𝑖
𝑒
𝑛
𝑐
𝑦
𝑆
𝑐
𝑜
𝑟
𝑒
)
MVES=0.6(ValueIndexScore)+0.4(MileageEfficiencyScore)
4️⃣ Insurance Burden Score (IBS) – 0–100

From: vehicleinsurance.csv

𝐼
𝑛
𝑠
𝑢
𝑟
𝑎
𝑛
𝑐
𝑒
𝐼
𝑛
𝑐
𝑜
𝑚
𝑒
𝑅
𝑎
𝑡
𝑖
𝑜
=
𝑃
𝑟
𝑒
𝑚
𝑖
𝑢
𝑚
𝐴
𝑛
𝑛
𝑢
𝑎
𝑙
𝑆
𝑎
𝑙
𝑎
𝑟
𝑦
InsuranceIncomeRatio=
AnnualSalary
Premium
	​

Ratio	Score
<3%	100
3–6%	75
6–10%	50
>10%	25

Adjust for claim probability.

5️⃣ Reliability Score (RS) – 0–100

From: vehiclerepairs.csv

𝑅
𝑒
𝑝
𝑎
𝑖
𝑟
𝐼
𝑛
𝑑
𝑒
𝑥
=
𝐻
𝑖
𝑔
ℎ
𝑆
𝑒
𝑣
𝑒
𝑟
𝑖
𝑡
𝑦
𝑅
𝑒
𝑝
𝑎
𝑖
𝑟
𝑠
𝑇
𝑜
𝑡
𝑎
𝑙
𝑅
𝑒
𝑝
𝑎
𝑖
𝑟
𝑠
RepairIndex=
TotalRepairs
HighSeverityRepairs
	​

𝐹
𝑟
𝑒
𝑞
𝑢
𝑒
𝑛
𝑐
𝑦
𝐼
𝑛
𝑑
𝑒
𝑥
=
𝑅
𝑒
𝑝
𝑎
𝑖
𝑟
𝑠
𝑃
𝑒
𝑟
𝑌
𝑒
𝑎
𝑟
𝐼
𝑛
𝑑
𝑢
𝑠
𝑡
𝑟
𝑦
𝐴
𝑣
𝑔
FrequencyIndex=
IndustryAvg
RepairsPerYear
	​

𝑅
𝑆
=
100
−
(
0.6
(
𝑅
𝑒
𝑝
𝑎
𝑖
𝑟
𝐼
𝑛
𝑑
𝑒
𝑥
𝑆
𝑐
𝑜
𝑟
𝑒
)
+
0.4
(
𝐹
𝑟
𝑒
𝑞
𝑢
𝑒
𝑛
𝑐
𝑦
𝐼
𝑛
𝑑
𝑒
𝑥
𝑆
𝑐
𝑜
𝑟
𝑒
)
)
RS=100−(0.6(RepairIndexScore)+0.4(FrequencyIndexScore))
6️⃣ Buyer Profile Fit Score (BPFS) – 0–100

From: carbuyers.csv

Based on:

Age cluster alignment

Gender popularity ratio

Segment popularity

Use clustering similarity:

𝐵
𝑃
𝐹
𝑆
=
𝐶
𝑜
𝑠
𝑖
𝑛
𝑒
𝑆
𝑖
𝑚
𝑖
𝑙
𝑎
𝑟
𝑖
𝑡
𝑦
(
𝑈
𝑠
𝑒
𝑟
𝑉
𝑒
𝑐
𝑡
𝑜
𝑟
,
𝑆
𝑒
𝑔
𝑚
𝑒
𝑛
𝑡
𝑉
𝑒
𝑐
𝑡
𝑜
𝑟
)
×
100
BPFS=CosineSimilarity(UserVector,SegmentVector)×100
📊 2. Composite Recommendation Score (CRS)

Now combine everything.

Your weighted framework:

Component	Weight
Financial Sustainability	30%
Loan Feasibility	20%
Market Value Efficiency	15%
Reliability	15%
Insurance Burden	10%
Buyer Profile Fit	10%
Final Formula
𝐶
𝑅
𝑆
=
0.30
(
𝐹
𝑆
𝑆
)
+
0.20
(
𝐿
𝐹
𝑆
)
+
0.15
(
𝑀
𝑉
𝐸
𝑆
)
+
0.15
(
𝑅
𝑆
)
+
0.10
(
𝐼
𝐵
𝑆
)
+
0.10
(
𝐵
𝑃
𝐹
𝑆
)
CRS=0.30(FSS)+0.20(LFS)+0.15(MVES)+0.15(RS)+0.10(IBS)+0.10(BPFS)
Interpretation
CRS	Recommendation
85–100	Strong Buy
70–84	Recommended
55–69	Moderate Risk
40–54	Financially Risky
<40	Not Recommended
🚀 3. Startup-Ready Architecture Diagram

Here is your production architecture:

                ┌─────────────────────────┐
                │   Streamlit Frontend    │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │   API Layer (FastAPI)   │
                └────────────┬────────────┘
                             │
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                    ▼
  Feature Engine       Scoring Engine        RAG Engine
  (Ratios & KPIs)      (CRS Calculator)     (Vector Search)
        │                    │                    │
        ▼                    ▼                    ▼
  PostgreSQL           Redis Cache          Vector DB (FAISS)
  (Structured Data)                         (Embeddings)
        │
        ▼
  Model Layer
  - ML ranking model
  - Clustering model
Recommended Tech Stack
Layer	Tech
Frontend	Streamlit
API	FastAPI
DB	PostgreSQL
Vector DB	FAISS / Weaviate
Caching	Redis
Orchestration	CrewAI
ML	Scikit-learn / XGBoost
🔎 4. RAG Retrieval Structure Per Dataset

Instead of dumping full CSV into LLM, chunk smartly.

Dataset 1: carpurchase.csv
Embedding Strategy:

Chunk by:

Income bands

Age clusters

Purchase amount ranges

Retriever Query:

"Buyer age 32, salary 80k, net worth 150k — similar purchase patterns?"
Dataset 2: carbuyers.csv

Chunk by:

Manufacturer

Gender split

Total purchase volume

Retriever Query:

"Most purchased SUVs by males 30–40 income bracket"
Dataset 3: loanapproval.csv

Chunk by:

Credit score bands

Approval outcome

Retriever Query:

"Loan approvals for credit score 680 with 3 dependents"
Dataset 4: usedcars.csv

Chunk by:

Make

Year range

Price band

Retriever Query:

"Best SUV under $25k with mileage < 60k"
Dataset 5: vehicleinsurance.csv

Chunk by:

Vehicle type

Engine CC

Claim paid flag

Retriever Query:

"Insurance premium trends for SUVs 2000cc personal use"
Dataset 6: vehiclerepairs.csv

Chunk by:

Car model

Severity

Problem classification

Retriever Query:

"Common high-severity issues for 2018 Toyota Corolla"
🏆 What You Now Have

You now own:

A quantitative scoring engine

A weighted composite model

A scalable architecture

A structured RAG retrieval strategy

An investor-grade intelligent auto recommendation framework
