import sys
import os
from pathlib import Path

# Перенаправление stdout и stderr в файлы
output_dir = Path('results')
output_dir.mkdir(exist_ok=True)

log_file = output_dir / 'execution_log.txt'
error_file = output_dir / 'error_log.txt'

# Открываем файлы для записи
sys.stdout = open(log_file, 'w', encoding='utf-8')
sys.stderr = open(error_file, 'w', encoding='utf-8')

print(f"\nДата запуска: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

try:
    exec(open('/Users/rizatkabdybek/Documents/Data/ml_lab.py').read())

    print(f"\nрезультаты в папке: {output_dir.absolute()}")
    print("\nФайлы:")
    print("  - figures/        : Графики и визуализации")
    print("  - data/           : Обработанные данные")
    print("  - reports/        : Текстовые отчеты")
    print("  - execution_log.txt : Лог выполнения")
    
except Exception as e:
    print(f"\n\nОШИБКА ПРИ ВЫПОЛНЕНИИ: {str(e)}", file=sys.stderr)
    import traceback
    traceback.print_exc(file=sys.stderr)
    
finally:
    sys.stdout.close()
    sys.stderr.close()
    
    # Выводим краткую информацию в консоль
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    
    print("\nАнализ завершен!")
    print(f"Результаты сохранены в: {output_dir.absolute()}")
    print("\nСозданные файлы:")
    
    # Подсчитываем файлы
    figures = list((output_dir / 'figures').glob('*')) if (output_dir / 'figures').exists() else []
    data_files = list((output_dir / 'data').glob('*')) if (output_dir / 'data').exists() else []
    reports = list((output_dir / 'reports').glob('*')) if (output_dir / 'reports').exists() else []
    
    print(f"   - Графиков: {len(figures)}")
    print(f"   - Данных: {len(data_files)}")
    print(f"   - Отчетов: {len(reports)}")
    print(f"\n Логи: {log_file}")
