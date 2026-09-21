import math
from math import fsum, ceil, floor
import sys

def main():
    durations = [
        0.1,
        0.1,
        0.1,
        0.1,
        0.1,
        0.1,
        0.1,
        0.1,
        0.1,
        0.1,
    ]

    # result_by_sum = sum(durations)
    # result_by_fsum = fsum(durations)
    # print(f"result_by_sum: {result_by_sum}")
    # print(f"result_by_fsum: {result_by_fsum}")
    # print(sys.version)

    # values = [
    #     -0.10430216751806065,
    #     -266310978.67179024,
    #     143401161448607.16,
    #     -143401161400469.7,
    #     266262841.31058735,
    #     -0.003244936839808227,
    # ]
    #
    #
    #
    # result_by_loop = 0
    # for el in values:
    #     result_by_loop += el
    # result_by_sum = sum(values)
    # result_by_fsum = fsum(values)
    # sum_and_fsum_difference = abs(result_by_sum - result_by_fsum)
    # loop_and_sum_difference = abs(result_by_loop - result_by_fsum)
    #
    #
    # print(f"result_by_loop: {result_by_loop}")
    # print(f"result_by_sum: {result_by_sum}")
    # print(f"result_by_fsum: {result_by_fsum}")
    # print(f"sum_and_fsum_difference: {sum_and_fsum_difference}")
    # print(f"loop_and_sum_difference: {loop_and_sum_difference}")

    # durations = [
    #     0.142,
    #     0.138,
    #     float("nan"),
    #     0.151,
    #     float("inf"),
    #     0.149,
    #     -float("inf"),
    #     0.140,
    # ]
    #
    # finite_durations = [duration for duration in durations if math.isfinite(duration)]
    # finite_count = len(finite_durations)
    # nan_count = len([duration for duration in durations if math.isnan(duration)])
    # inf_count = len([duration for duration in durations if math.isinf(duration)])
    # has_invalid_values = len(durations) != finite_count
    # finite_total  = fsum(finite_durations)
    #
    # print(f"finite_count: {finite_count}")
    # print(f"nan_count: {nan_count}")
    # print(f"inf_count: {inf_count}")
    # print(f"has_invalid_values: {has_invalid_values}")
    # print(f"finite_total: {finite_total}")

    # values_1 = [
    #     0.18,
    #     float("nan"),
    #     0.12,
    #     0.25,
    #     0.15,
    # ]
    #
    # values_2 = [
    #     float("nan"),
    #     0.18,
    #     0.12,
    #     0.25,
    #     0.15,
    # ]
    #
    # nan = float("nan")
    # print(nan == nan)
    # print(nan < 0.20)
    # print(nan > 0.20)
    #
    # min_value_1 = min(values_1)
    # min_value_2 = min(values_2)
    # print(min_value_1)
    # print(min_value_2)
    #
    # max_value_1 = max(values_1)
    # max_value_2 = max(values_2)
    # print(max_value_1)
    # print(max_value_2)
    #
    # durations = [
    #     0.241,
    #     float("nan"),
    #     0.198,
    #     float("inf"),
    #     0.315,
    #     0.204,
    #     -float("inf"),
    #     0.227,
    # ]
    #
    # finite_durations = [duration for duration in durations if math.isfinite(duration)]
    # min_duration = min(finite_durations)
    # max_duration = max(finite_durations)
    # duration_range = max_duration - min_duration
    # average_duration = fsum(finite_durations) / len(finite_durations)
    # invalid_count = len(durations) - len(finite_durations)
    #
    # print(f"finite_durations: {finite_durations}")
    # print(f"min_duration: {min_duration}")
    # print(f"max_duration: {max_duration}")
    # print(f"duration_range: {duration_range}")
    # print(f"average_duration: {average_duration}")
    # print(f"invalid_count: {invalid_count}")
    #
    # durations = [
    #     float("nan"),
    #     float("inf"),
    #     -float("inf"),
    # ]
    #
    # finite_durations = [
    #     duration
    #     for duration in durations
    #     if math.isfinite(duration)
    # ]
    #
    # # print(min(finite_durations))
    # # print(max(finite_durations))
    # print(fsum(finite_durations))

    # durations = [
    #     float("nan"),
    #     float("inf"),
    #     -float("inf"),
    # ]
    #
    # finite_durations = [duration for duration in durations if math.isfinite(duration)]
    # finite_duration_count = len(finite_durations)
    # min_duration = min(finite_durations) if finite_duration_count else None
    # max_duration = max(finite_durations) if finite_duration_count else None
    # average_duration = fsum(finite_durations) / finite_duration_count if finite_duration_count else None
    # invalid_count = len(durations) - finite_duration_count
    #
    # print(f"finite_durations: {finite_durations}")
    # print(f"min_duration: {min_duration}")
    # print(f"max_duration: {max_duration}")
    # print(f"average_duration: {average_duration}")
    # print(f"invalid_count: {invalid_count}")

    total_tests = 118
    tests_per_batch = 25
    max_parallel_batches = 4

    average_batch_duration = 7.8
    timeout_multiplier = 1.25

    min_timeout = 5
    max_timeout = 10

    required_batches = ceil(total_tests / tests_per_batch)
    parallel_batches = min(required_batches, max_parallel_batches)
    required_waves = ceil(required_batches / max_parallel_batches)
    whole_duration = floor(average_batch_duration)
    raw_timeout = average_batch_duration * timeout_multiplier
    timeout = max(min(ceil(raw_timeout), max_timeout), min_timeout)

    print(f"required_batches: {required_batches}")
    print(f"parallel_batches: {parallel_batches}")
    print(f"required_waves: {required_waves}")
    print(f"whole_duration: {whole_duration}")
    print(f"raw_timeout: {raw_timeout}")
    print(f"timeout: {timeout}")
if __name__ == '__main__':
    main()


