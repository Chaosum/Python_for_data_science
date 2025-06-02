def ft_tqdm(lst: range):
    total = len(lst)
    bar_length = 100
    for i, item in enumerate(lst, 1):
        percent = i / total
        filled_length = int(bar_length * percent)
        bar = '=' * filled_length + '>' \
            + ' ' * (bar_length - filled_length - 1)
        # windows
        # bar = '' * filled_length \
        #     + ' ' * (bar_length - filled_length)
        print(
            f"\r{int(percent * 100):3}%|[{bar}]| {i}/{total}",
            end='', flush=True
        )
        yield item
    print()
