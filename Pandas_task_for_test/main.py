import pandas as pd
import numpy as np
import json
from datetime import datetime as dt



df = pd.read_csv('players_22.csv', low_memory=False)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


df_copy = df.copy()

print(df_copy.head())
total_rows = df_copy.shape[0]
total_columns = df_copy.shape[1]
wage_eur = df_copy.dtypes['wage_eur']
columns_for_drop =  ['club_position',
 'club_jersey_number',
 'club_loaned_from',
 'club_joined',
 'club_contract_valid_until',
 'nationality_id',
 'nationality_name',
 'nation_team_id',
 'nation_position',
 'nation_jersey_number',
 'preferred_foot',
 'weak_foot',
 'skill_moves',
 'international_reputation',
 'work_rate',
 'body_type',
 'real_face',
 'release_clause_eur',
 'player_tags',
 'player_traits',
 'pace',
 'shooting',
 'passing',
 'dribbling',
 'defending',
 'physic',
 'attacking_crossing',
 'attacking_finishing',
 'attacking_heading_accuracy',
 'attacking_short_passing',
 'attacking_volleys',
 'skill_dribbling',
 'skill_curve',
 'skill_fk_accuracy',
 'skill_long_passing',
 'skill_ball_control',
 'movement_acceleration',
 'movement_sprint_speed',
 'movement_agility',
 'movement_reactions',
 'movement_balance',
 'power_shot_power',
 'power_jumping',
 'power_stamina',
 'power_strength',
 'power_long_shots',
 'mentality_aggression',
 'mentality_interceptions',
 'mentality_positioning',
 'mentality_vision',
 'mentality_penalties',
 'mentality_composure',
 'defending_marking_awareness',
 'defending_standing_tackle',
 'defending_sliding_tackle',
 'goalkeeping_diving',
 'goalkeeping_handling',
 'goalkeeping_kicking',
 'goalkeeping_positioning',
 'goalkeeping_reflexes',
 'goalkeeping_speed',
 'ls',
 'st',
 'rs',
 'lw',
 'lf',
 'cf',
 'rf',
 'rw',
 'lam',
 'cam',
 'ram',
 'lm',
 'lcm',
 'cm',
 'rcm',
 'rm',
 'lwb',
 'ldm',
 'cdm',
 'rdm',
 'rwb',
 'lb',
 'lcb',
 'cb',
 'rcb',
 'rb',
 'gk',
 'player_face_url',
 'club_logo_url',
 'club_flag_url',
 'nation_logo_url',
 'nation_flag_url']
print(f"Количество наблюдений: {total_rows}")
print(f"Количество признаков: {total_columns}")
print(f"Тип данных age_eur: {wage_eur}")

df_copy.drop(columns=columns_for_drop, inplace=True)

print(df_copy.head())
print(df_copy.shape)
duplicate_count = df_copy.duplicated().sum()
duplicate_count_short_age = (df_copy.duplicated(subset=['short_name', 'age'], keep=False).sum())
dublicate_count_long_club = (df_copy.duplicated(subset=['long_name','club_name'], keep=False).sum())

print(f"Количество полных дубликатов: {duplicate_count}")
print(f"Количество дубликатов по признакам short_name,age: {duplicate_count_short_age}")
print(f"Количество дубликатов по признакам long_name, club_name: {dublicate_count_long_club}")

df_copy.drop_duplicates(subset=['long_name','club_name'], keep=False, inplace=True)

print(f"Количетсво строк после удаления дубликатов: {df_copy.shape[0]}" )

print(df_copy.isnull().sum())

missing_values_value_eur = df_copy['value_eur'].isnull().sum()
procent_missing = (missing_values_value_eur / total_rows) * 100

print(f"Процент пропущенных значений value_eur: {procent_missing:.2f}")

procent_full_league_name = (total_rows - df_copy['league_name'].isnull().sum())

print(f"Количество заполненных значений league_name: {procent_full_league_name}")

df_copy.dropna(subset=['club_name'],inplace=True)
print(df_copy.shape)
# print(df_copy.isnull().sum())
count_missing_value_eur = df_copy['value_eur'].isnull().sum()
print(f"Количество пропущенных значений по признаку value_eur: {count_missing_value_eur}")

mean = df_copy['value_eur'].mean()
print(f"Среднее значение value_eur: {mean:.2f}")
df_copy['value_eur'] = df_copy['value_eur'].fillna(mean)
df_copy.reset_index(drop=True, inplace=True)
print(df_copy.info())

dob = df_copy['dob'].dtype
print(f"Тип данных dob: {dob}")
df_copy.dob = pd.to_datetime(df_copy.dob, format='%Y-%m-%d',dayfirst=True)
# df_copy.dob = df_copy.dob.dt.strftime('%d-%m-%Y')
print(df_copy['dob'].head())
print(f"Тип данных dob: {dob}")

overall = df_copy['overall'].dtype
print(f"Тип данных overall: {overall}")
df_copy.overall = pd.to_numeric(df_copy.overall ,downcast='float')


value_eur = df_copy['value_eur'].dtype
print(f"Тип данных value_eur: {value_eur}")
df_copy.value_eur = df_copy.value_eur.astype('int')

print(df_copy.age.head())
current_year = dt.now().year
df_copy['age_new'] = current_year - df_copy.dob.apply(lambda x: x.year)
print(df_copy.age_new.head())

print(df_copy.columns)


