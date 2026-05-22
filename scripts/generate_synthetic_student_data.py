from pathlib import Path

import numpy as np
import pandas as pd


def generate_synthetic_student_data(n_rows: int = 2000, random_seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(random_seed)

    cohort_year = rng.choice([2021, 2022, 2023, 2024], size=n_rows, p=[0.2, 0.3, 0.3, 0.2])
    program = rng.choice(
        ["Education", "Psychology", "Economics", "Computer Science", "Public Health"],
        size=n_rows,
        p=[0.22, 0.2, 0.2, 0.23, 0.15],
    )
    semester = rng.integers(1, 9, size=n_rows)

    internet_access = rng.choice(["stable", "limited", "unstable"], size=n_rows, p=[0.7, 0.2, 0.1])
    part_time_work_hours = np.clip(rng.normal(10, 7, size=n_rows), 0, 40)
    commute_minutes = np.clip(rng.normal(35, 18, size=n_rows), 0, 120)
    ai_tool_usage_frequency = rng.choice(
        ["never", "rarely", "sometimes", "often", "very_often"],
        size=n_rows,
        p=[0.08, 0.2, 0.37, 0.25, 0.1],
    )

    previous_gpa = np.clip(rng.normal(3.0, 0.45, size=n_rows), 1.5, 4.0)
    study_hours_base = rng.normal(12, 4.5, size=n_rows)
    study_hours_per_week = np.clip(study_hours_base - 0.08 * part_time_work_hours, 0, 40)

    attendance_rate = np.clip(
        rng.normal(82, 10, size=n_rows)
        + (previous_gpa - 3.0) * 6
        - (commute_minutes / 120) * 5
        + np.where(internet_access == "stable", 1.5, -2.0),
        35,
        100,
    )

    submission_delay_days = np.clip(
        rng.poisson(1.5, size=n_rows) + np.where(part_time_work_hours > 20, 1, 0),
        0,
        20,
    ).astype(float)

    lms_logins = np.clip(
        rng.normal(35, 11, size=n_rows) + study_hours_per_week * 0.9 + attendance_rate * 0.1,
        2,
        120,
    )

    assignment_score = np.clip(
        45
        + 0.28 * attendance_rate
        + 1.1 * study_hours_per_week
        + (previous_gpa - 2.5) * 8
        - 1.2 * submission_delay_days
        + rng.normal(0, 6, size=n_rows),
        30,
        100,
    )

    quiz_average = np.clip(
        40
        + 0.3 * attendance_rate
        + 0.5 * study_hours_per_week
        + (previous_gpa - 2.5) * 8
        + rng.normal(0, 7, size=n_rows),
        25,
        100,
    )

    midterm_score = np.clip(
        35
        + 0.35 * attendance_rate
        + 0.35 * quiz_average
        + 0.2 * assignment_score
        + rng.normal(0, 8, size=n_rows),
        20,
        100,
    )

    final_exam_score = np.clip(
        30
        + 0.3 * attendance_rate
        + 0.25 * quiz_average
        + 0.25 * midterm_score
        + (previous_gpa - 2.5) * 10
        + rng.normal(0, 8, size=n_rows),
        20,
        100,
    )

    final_grade = np.clip(
        0.18 * attendance_rate
        + 0.22 * assignment_score
        + 0.18 * quiz_average
        + 0.2 * midterm_score
        + 0.22 * final_exam_score
        + (previous_gpa - 3.0) * 5
        + rng.normal(0, 3, size=n_rows),
        0,
        100,
    )

    passed = (final_grade >= 60).astype(int)

    df = pd.DataFrame(
        {
            "student_id": [f"S{100000 + i}" for i in range(n_rows)],
            "cohort_year": cohort_year,
            "program": program,
            "semester": semester,
            "attendance_rate": attendance_rate.round(2),
            "assignment_score": assignment_score.round(2),
            "quiz_average": quiz_average.round(2),
            "midterm_score": midterm_score.round(2),
            "final_exam_score": final_exam_score.round(2),
            "lms_logins": np.round(lms_logins).astype(int),
            "study_hours_per_week": study_hours_per_week.round(2),
            "internet_access": internet_access,
            "part_time_work_hours": part_time_work_hours.round(2),
            "commute_minutes": commute_minutes.round(2),
            "ai_tool_usage_frequency": ai_tool_usage_frequency,
            "previous_gpa": previous_gpa.round(2),
            "final_grade": final_grade.round(2),
            "passed": passed,
            "submission_delay_days": submission_delay_days.round(2),
            "missing_reason_flag": rng.choice(["none", "self_report_missing", "system_issue"], size=n_rows, p=[0.86, 0.1, 0.04]),
        }
    )

    # Non-random missingness to support cleaning practice.
    limited_or_unstable = df["internet_access"].isin(["limited", "unstable"])
    high_workload = df["part_time_work_hours"] > 25

    missing_final_exam_mask = limited_or_unstable & (rng.random(n_rows) < 0.07)
    missing_study_hours_mask = high_workload & (rng.random(n_rows) < 0.08)
    missing_quiz_mask = (df["submission_delay_days"] > 6) & (rng.random(n_rows) < 0.06)

    df.loc[missing_final_exam_mask, "final_exam_score"] = np.nan
    df.loc[missing_study_hours_mask, "study_hours_per_week"] = np.nan
    df.loc[missing_quiz_mask, "quiz_average"] = np.nan

    duplicate_indices = rng.choice(df.index, size=12, replace=False)
    duplicates = df.loc[duplicate_indices].copy()
    final_df = pd.concat([df, duplicates], ignore_index=True)

    return final_df


def main() -> None:
    output_path = Path("data/synthetic/synthetic_student_performance.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    data = generate_synthetic_student_data(n_rows=2000, random_seed=42)
    data.to_csv(output_path, index=False)

    print(f"Saved synthetic dataset to: {output_path}")
    print(f"Rows: {data.shape[0]}, Columns: {data.shape[1]}")


if __name__ == "__main__":
    main()
