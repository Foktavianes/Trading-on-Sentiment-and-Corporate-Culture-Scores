"""Aggregate scores to firm-year level (optional)
Scores are adjusted by document length (100*score/length)
"""

import global_options
import pandas as pd
from pathlib import Path

print("Aggregating scores to firms and adjusting by document lengths.")

id2firm = pd.read_csv(str(Path(global_options.DATA_FOLDER, "input", "filtered_data_short.csv")))

methods = ["TF", "TFIDF", "WFIDF"]
for method in methods:
    scores = pd.read_csv(
        str(
            Path(global_options.OUTPUT_FOLDER, "scores", "scores_{}.csv".format(method))
        )
    )

    scores.dropna(axis =0, inplace=True) #drop rows with na

    scores = scores.merge(
    id2firm, how="left", left_on=["Doc_ID"], right_on="document_id"
    ).drop(["Doc_ID", "document_id"], axis=1)
    for dim in global_options.DIMS:
        scores[dim] = 100 * scores[dim] / scores["document_length"]    #Output separate culture value result -> can try different combinations for total cultural score to maximise trading strategy returns

    # scores = scores.concat([scores, id2firm],
    #                        axis = 1,
    #                        join = 'inner',
    #                        )

    scores.groupby(["firm_id", "time"]).mean()
    scores.sort_values(by=["firm_id", "time"], ascending=[True, True])
    scores.to_csv(
        str(
            Path(
                global_options.OUTPUT_FOLDER,
                "scores",
                "firm_scores_{}.csv".format(method),
            )
        ),
        index=False,
        float_format="%.4f",
    )

